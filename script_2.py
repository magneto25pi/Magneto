import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

lat = open( 'lat_si_long/lat.txt', 'r' )
lon = open( 'lat_si_long/long.txt', 'r' )
mx = open( 'magn/date_magn/date_magnetometru_x.txt', 'r' )
my = open( 'magn/date_magn/date_magnetometru_y.txt', 'r' )
mz = open( 'magn/date_magn/date_magnetometru_z.txt', 'r' )
mg = open( 'magn/date_magn/date_magnetometru_totale.txt', 'a' )

x = []
y = []

for i in lat:
	y.append( float( i ) )

for j in lon:
	x.append( float( j ) )

#plt.xlabel( 'longitude' )
#plt.ylabel( 'latitude' )
#plt.plot( x, y, 'o' )

mgx = []
mgy = []
mgz = []
for i in mx:
	mgx.append( float( i ) )
for i in my:
	mgy.append( float( i ) )
for i in mz:
	mgz.append( float( i ) )

x1 = np.linspace(-200, 200, 10)

mgt = []
maxx = 0
ind = 0
for i in range(0, 689):
	mgt.append( math.sqrt( mgx[i]**2 + mgy[i]**2 + mgz[i]**2 ) )
	if mgt[i] > maxx and i >= 2:
		maxx = mgt[i]
		ind = i
	mg.write( str( mgt[i] ) + '\n' )

print( str( maxx ) + ' ' + str( ind ) )



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D( x, y, 0, 'o' )
ax.plot3D( x, y, mgt, 'rx' )
plt.xlabel( 'longitude (°)' )
plt.ylabel( 'latitude (°)' )
ax.set_zlabel( 'magnetic field intensity (μT)' )

#plt.plot( y, mgt, 'o' )
#plt.xlabel( 'latitude (°)' )
#plt.ylabel( 'magnetic intensity (μT)' )
plt.show()