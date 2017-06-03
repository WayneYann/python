"""
Calculate atmospheric pressure at altitude.
"""

import numpy as np


def standardtemperature(geopot_height):
    """
    Standard temperature at elevation.
    """
    stdtemp = None  # initiate standard temperature variable

    if geopot_height <= 11:
        # Troposphere
        stdtemp = 288.15 - (6.5 * geopot_height)
    elif geopot_height <= 20:
        # Stratosphere starts
        stdtemp = 216.65
    elif geopot_height <= 32:
        stdtemp = 196.65 + geopot_height
    elif geopot_height <= 47:
        stdtemp = 228.65 + 2.8 * (geopot_height - 32)
    elif geopot_height <= 51:
        # Mesosphere starts
        stdtemp = 270.65
    elif geopot_height <= 71:
        stdtemp = 270.65 - 2.8 * (geopot_height - 51)
    elif geopot_height <= 84.85:
        stdtemp = 214.65 - 2 * (geopot_height - 71)
    else:
        raise ValueError('geopot_height must be less than 84.85 km')

    return stdtemp


def atmosphere(altitude):
    """
    Calculate atmospheric pressure at altitude.
    See article at https://en.wikipedia.org/wiki/Barometric_formula
    """
    altitude = altitude / 1000  # convert altitude in m to km

    earth_radius = 6356.766     # radius of the earth, km
    geopot_height = (earth_radius * altitude) / (earth_radius + altitude)
    t = standardtemperature(geopot_height)

    atmpress = None     # initialize variable for atmospheric pressure

    if geopot_height <= 11:
        atmpress = 101325 * pow(288.15/t, -5.255877)
    elif geopot_height <= 20:
        atmpress = 22632.06 * np.exp(-0.1577 * (geopot_height - 11))
    elif geopot_height <= 32:
        atmpress = 5474.889 * pow(216.65/t, 34.16319)
    elif geopot_height <= 47:
        atmpress = 868.0187 * pow(228.65/t, 12.2011)
    elif geopot_height <= 51:
        atmpress = 110.9063 * np.exp(-0.1262 * (geopot_height - 47))
    elif geopot_height <= 71:
        atmpress = 66.93887 * pow(270.65/t, -12.2011)
    elif geopot_height <= 84.85:
        atmpress = 3.956420 * pow(214.65/t, -17.0816)
    else:
        raise ValueError('altitude must be less than 86 km')

    return atmpress


elev_golden = 1729.74   # elevation of Golden CO, m
patm_golden = atmosphere(elev_golden)

print('patm =', patm_golden, 'Pa')

