import matplotlib.pyplot as plt
import numpy as np

a = open( 'altitude/altitude_final.txt', 'r' )
m1 = open( 'magn/date_magn/date_magnetometru_x.txt', 'r' )
m2 = open( 'magn/date_magn/date_magnetometru_y.txt', 'r' )
m3 = open( 'magn/date_magn/date_magnetometru_z.txt', 'r' )

x = []
y = [] # altitude
# magnetic intensity 1, 2, 3.
y1 = []
y2 = []
y3 = []

cnt = 0
for i in a:
	y.append( float( i ) )
	x.append( cnt )
	cnt += 15;

for i in m1:
	y1.append( float( i )  )

for i in m2:
	y2.append( float( i )  )

for i in m3:
	y3.append( float( i )  )


#plt.plot( x, y)
#plt.plot( x, y3, 'b' )
#plt.xlabel( 'time (s)' )
#plt.ylabel( 'altitude (m)' )
#plt.show()

fig, ax1 = plt.subplots()

color = 'red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('altitude (m)', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 

color = 'tab:blue'
ax2.set_ylabel('magnetic field intensity (μT) on z axis', color=color) 
ax2.plot(x, y3, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()

a.close()
m1.close()
m2.close()
m3.close()