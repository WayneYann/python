"""
Compare different approaches to calculate volumes within a sphere. The sphere is
comprised of an inner center sphere with multiple shells around it. This approach
is used to calculate the volume average temprature of the entire sphere.
"""

import numpy as np

# Functions to Calculate Inner Sphere and Outer Shell Volumes
# -----------------------------------------------------------------------------

def vol1(rad):
    v0 = (4/3)*np.pi*(rad[0]**3)    # volume of inner center sphere, mm^3
    v = []                          # list to store volumes, mm^3
    v.append(v0)                    # add center sphere volume to volumes list

    # calculate each shell volume and store it in volumes list
    for i in rad[:-1]:
        ri = i
        ro = i+dr
        vshell = (4/3)*np.pi*(ro**3) - (4/3)*np.pi*(ri**3)
        v.append(vshell)

    return v    # return list of volumes


def vol2(rad):
    ro = rad                    # outer radii, mm
    ri = np.zeros(len(rad))     # inner radii array, mm
    ri[1:] = rad[0:-1]          # zero as first element of inner radii array
    v = (4/3)*np.pi*(ro**3) - (4/3)*np.pi*(ri**3)   # calculate volumes
    return v                    # return vector of volumes


def vol3(rad):
    vrad = (4/3)*np.pi*(rad**3) # volumes of all spheres
    vi = np.zeros(len(rad))     # store inner radii
    vi[1:] = vrad[0:-1]         # volumes for inner radii
    v = vrad - vi               # calculate center sphere and shell volumes
    return v                    # return vector of volumes


def vol4(rad):
    vrad = (4/3)*np.pi*(rad**3)     # volumes of all spheres
    vi = np.insert(vrad[:-1], 0, 0) # store inner radii
    v = vrad - vi                   # calculate center sphere and shell volumes
    return v                        # return vector of volumes


def vol5(rad2):
    vr = (4/3)*np.pi*(rad2**3)  # volume of each sphere at each radius
    v = vr[1:] - vr[0:-1]       # center sphere volume and outer shell volumes
    return v                    # return vector of volumes


# Calculate Volumes
# -----------------------------------------------------------------------------

d = 3       # diameter of sphere, mm
r = d/2     # radius of sphere, mm

m = 10000   # number of nodes from sphere center (m=0) to surface (m)
# m = 5       # number of nodes from sphere center (m=0) to surface (m)
nr = m-1    # number of radius steps
dr = r/nr   # radius step as delta r, mm

rad = np.linspace(dr, r, nr)   # array of each radius step, mm
rad2 = np.linspace(0, r, m) # array of each radius starting at center, mm

# Calculate volume array from each approach using a vector of radii
v1 = vol1(rad)      # list of volumes from approach 1
v2 = vol2(rad)      # array of volumes from approach 2
v3 = vol3(rad)      # array of volumes from approach 3
v4 = vol4(rad)      # array of volumes from approach 4
v5 = vol5(rad2)     # array of volumes from approach 5

# Print Volume Results
# -----------------------------------------------------------------------------

# display volumes from each approach, use for small m such as m=5
# print('volumes v1', v1)
# print('volumes v2', v2)
# print('volumes v3', v3)
# print('volumes v4', v4)
# print('volumes v5', v5)

# sum of all volumes should equal volume of entire sphere
print('volumes v1 sum', sum(v1))
print('volumes v2 sum', v2.sum())
print('volumes v3 sum', v3.sum())
print('volumes v4 sum', v4.sum())
print('volumes v5 sum', v5.sum())

# check results based on volumes of entire sphere, center sphere, surface shell
V = (np.pi/6)*(d**3)                            # volume of entire sphere, mm^3
v0 = (4/3)*np.pi*(dr**3)                            # center sphere volume, mm^3
vR = (4/3)*np.pi*(r**3) - (4/3)*np.pi*((r-dr)**3)   # surface shell volume, mm^3

print('V of entire sphere = {} mm^3'.format(V))
print('v0, center sphere volume is', v0)
print('vR, surface shell volume is', vR)

# Calculate Volume Average (Mean) Temperature of Entire Sphere
# -----------------------------------------------------------------------------

def Tvol(T, Vs):
    """
    Use center sphere volume and shell volumes as weights to calculate the
    volume average temperature of entire sphere.
    Parameters:
    T = vector of temperatures at each node point, K
    Vs = center and subsequent shell volumes in sphere, m^3
    Returns:
    Tv = volume average temperature of sphere as a weighted mean, K
    """
    Tavg = (T[:-1] + T[1:]) / 2 # average temperature between each node point
    Tv = np.average(Tavg, weights=Vs)   # volume average weighted temperature
    return Tv

# parameters for calculating volume average temperature
d = 3       # diameter of sphere, mm
r = d/2     # radius of sphere, mm
m = 10      # number of nodes from sphere center (m=0) to surface (m)
nr = m-1    # number of radius steps
dr = r/nr   # radius step as delta r, mm

# new radius and volume array
rads = np.linspace(dr, r, nr)   # array of each radius step, mm
vols = vol3(rads)               # array of volumes from approach 3

# list of temperatures at each node point within sphere
T = np.array([273, 300, 340, 380, 460, 500, 550, 600, 660, 773])

# volume average temperature based on weighted mean
Tv_weight = Tvol(T, vols)

# volume average temperature calculated as mean
Tv_mean = np.mean(T)

# Print Temperature Results
# -----------------------------------------------------------------------------

print('Tv as weighted mean is', Tv_weight)
print('Tv as mean is', Tv_mean)
