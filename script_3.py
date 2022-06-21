import matplotlib.pyplot as plt

p = open( 'pressure/pres.txt', 'r' )

x = []
y = []

cnt = 0
for i in p:
	x.append( cnt )
	y.append( float( i ) )
	cnt += 15

plt.ylabel( 'pressure (mbar)' )
plt.xlabel( 'time (s)' )
plt.plot( x, y )
plt.show()
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

sls = open( 'pressure/solar_wind/sls/speed.txt', 'r' )
slt = open( 'pressure/solar_wind/sls/time.txt', 'r' )

x = []
y = []

for i in sls:
	y.append( float( i ) )

for j in slt:
	x.append( float( j ) )

plt.ylabel( 'solar wind speed (km/s)' )
plt.xlabel( 'time (s)' )
plt.plot( x, y )
plt.show()'''

'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

el = open( 'elev_iss/elev_iss.txt' )

x = []
y = []

cnt = 0
for i in el:
	y.append( float( i ) )
	x.append( cnt )
	cnt += 15

plt.ylim( 300, 550 )
plt.rcParams["figure.figsize"] = [10.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.xlabel( 'time (s)' )
plt.ylabel( 'elevation (km)' )
plt.plot( x, y )
plt.show()'''