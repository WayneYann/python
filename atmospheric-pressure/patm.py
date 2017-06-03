"""
Calculate atmospheric pressure at altitude and plot for a range of heights.

References:
https://en.wikipedia.org/wiki/Barometric_formula
https://www.eoas.ubc.ca/books/Practical_Meteorology/ starting on page 11
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np

# Function
# ------------------------------------------------------------------------------

def pressure(alt):
    """
    Atmospheric pressure at altitude.
    
    Parameters
    ----------
    alt = altitude or elevation above sea level, m

    Returns
    -------
    Patm = atmospheric pressure, Pa
    """
    alt = alt/1000              # convert altitude from meters to kilometers
    Ro = 6356.766               # average radius of the Earth, km
    H = (Ro * alt)/(Ro + alt)   # geopotential height, km

    Patm = None     # initiate pressure variable

    if H <= 11:
        T = 288.15 - (6.5 * H)
        Patm = 101325 * (288.15 / T) ** (-5.255877)
    elif H <= 20:
        T = 216.65
        Patm = 22632 * np.exp(-0.1577 * (H - 11))
    elif H <= 32:
        T = 216.65 + (H - 20)
        Patm = 5474.9 * (216.65 / T) ** (34.16319)
    elif H <= 47:
        T = 228.65 + 2.8 * (H - 32)
        Patm = 868 * (228.65 / T) ** 12.2011
    elif H <= 51:
        T = 270.65
        Patm = 110.9 * np.exp(-0.1262 * (H - 47))
    else:
        raise ValueError('geopotential height must be less than 51 km')

    # return atmospheric pressure at altitude, Pa
    return Patm


# Calculations
# ------------------------------------------------------------------------------

alt = 1729.74           # elevation of Golden CO in meters
patm = pressure(alt)    # atmospheric pressure, Pa

print('patm =', patm, 'Pa')

# Plot
# ------------------------------------------------------------------------------

h = np.linspace(0, 51000)

patm = []
for a in h:
    p = pressure(a)
    patm.append(p)

plt.ion()
plt.close('all')
plt.style.use('ggplot')

plt.figure(1)
plt.plot(patm, h/1000, lw=2)
plt.xlabel('Pressure (Pa)')
plt.ylabel('Altitude (km)')
ax = plt.gca()
ax.get_xaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))

