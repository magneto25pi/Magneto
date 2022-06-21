import matplotlib.pyplot as plt
import magpylib as magpy
import numpy as np
from matplotlib import pyplot as plt
import time
import geopandas as gpd

R = 6371000000

lt = open( '/Users/stefanmatei/astro pi/date/analiza date/lat_si_long/lat.txt', 'r' )
lg = open( '/Users/stefanmatei/astro pi/date/analiza date/lat_si_long/long.txt', 'r' )

lat = []
long = []

for i in lt:
    lat.append( float( i ) )

for i in lg:
    long.append( float( i ) )

mx = -0.40e28  # in mT mm3 
my =  -2.39e28
mz = -7.04e28

rx = -0.01e9 # in mm
ry = -0.28e9
rz = 0.40e9

x1 = magpy.misc.Dipole((mx, my, mz), (rx, ry, rz))

xlist = np.linspace( -180, 180, 90 ) # longitude
ylist = np.linspace( -90, 90, 45 ) # latitude
X, Y = np.meshgrid( xlist, ylist )

Z = X.copy()

maxx = 0
latm = 0
longm = 0

maxx2 = 0
latm2 = 0
longm2 = 0

for i in range( 0, 45 ):
    for j in range( 0, 90 ):
        x = R * np.cos( np.deg2rad( Y[i][j] ) ) * np.cos( np.deg2rad( X[i][j] ) )
        y = R * np.cos( np.deg2rad( Y[i][j] ) ) * np.sin( np.deg2rad( X[i][j] ) )
        z = R * np.sin( np.deg2rad( Y[i][j] ) )

        B = x1.getB((x, y, z))

        b_fin = 0
        for t in range(0, 3):
            b_fin += B[t]**2
        b_fin = np.sqrt( b_fin )
        b_fin *= 1000
        Z[i][j] = b_fin
        if Y[i][j] < 0:
            if b_fin > maxx2:
                maxx2 = b_fin
                latm2 = Y[i][j]
                longm2 = X[i][j]
        else:
            if b_fin > maxx:
                maxx = b_fin
                latm = Y[i][j]
                longm = X[i][j]


print( maxx ) # South pole
print( latm )
print( longm )
print( '\n' )
print( maxx2 ) # North pole
print( latm2 )
print( longm2 )

fig = plt.figure(figsize=(10,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

levels=[10, 15, 20, 25, 30, 35, 40, 45, 50]
cp = ax.contour(X, Y, Z, levels)
ax.clabel(cp, inline=True, fontsize=10)
ax.set_xlabel('longitude (°)')
ax.set_ylabel('latitude (°)')

plt.colorbar(cp, shrink = 0.8, label='Magnetic field intensity (μT)')

plt.plot( long, lat, 'o' )

plt.plot( longm, latm, 'o' )
plt.plot( longm2, latm2, 'o' )

worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
worldmap.plot(color="lightgrey", ax=ax)

plt.show()
