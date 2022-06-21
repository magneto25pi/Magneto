import matplotlib.pyplot as plt
import magpylib as magpy
import numpy as np
from matplotlib import pyplot as plt
import time

R = 6371000000

mgn = open( '/Users/stefanmatei/astro pi/date/analiza date/magn/date_magn/date_magnetometru_totale.txt', 'r' )
lat = open( '/Users/stefanmatei/astro pi/date/analiza date/lat_si_long/lat.txt', 'r' )
longg = open( '/Users/stefanmatei/astro pi/date/analiza date/lat_si_long/long.txt', 'r' )
initial = open( '/Users/stefanmatei/astro pi/date/analiza date/gasirea_polilor/metoda1/initial.txt', 'r' )

mgt = []
lt = []
lg = []
b = []
bi = []
xa = []

cnt = 0
for i in mgn:
    mgt.append( float( i ) )
    xa.append( cnt )
    cnt += 15
for i in lat:
    lt.append( float( i ) )
for i in longg:
    lg.append( float( i ) )
for i in initial:
    bi.append( float( i ) )

least = -1
mlx = 0
mly = 0
mlz = 0
rlx = 0
rly = 0
rlz = 0
def main( max, may, maz, rax, ray, raz ):
    sum = 0
    global least
    global mlx
    global mly
    global mlz
    global rlx
    global rly
    global rlz


    x1 = magpy.misc.Dipole((max, may, maz), (rax, ray, raz))
    
    for i in range( 0, 689 ):
        x = R * np.cos( np.deg2rad( lt[i] ) ) * np.cos( np.deg2rad( lg[i] ) )
        y = R * np.cos( np.deg2rad( lt[i] ) ) * np.sin( np.deg2rad( lg[i] ) )
        z = R * np.sin( np.deg2rad( lt[i] ) )

        B = magpy.getB(x1, (x, y, z))
        b_fin = 0
        for i in range(0, 3):
            b_fin += B[i]**2
        b_fin = np.sqrt( b_fin )
        b_fin *= 1000

        b.append( b_fin )
        sum += ( mgt[i] - b_fin )**2

    if least == -1 or least > sum:
        least = sum
        mlx = max
        mly = may
        mlz = maz
        rlx = rax
        rly = ray
        rlz = raz

    '''
    fig, ax1 = plt.subplots()

    color = 'red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('magnetic intensity 1', color=color)
    ax1.plot(xa, bi, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('magnetic intensity 2', color=color)  # we already handled the x-label with ax1
    ax2.plot(xa, mgt, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.plot( xa, b, color='green' )

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()'''

    b.clear()

def printMinim():
    x1 = magpy.misc.Dipole((mlx, mly, mlz), (rlx, rly, rlz))
    
    for i in range( 0, 689 ):
        x = R * np.cos( np.deg2rad( lt[i] ) ) * np.cos( np.deg2rad( lg[i] ) )
        y = R * np.cos( np.deg2rad( lt[i] ) ) * np.sin( np.deg2rad( lg[i] ) )
        z = R * np.sin( np.deg2rad( lt[i] ) )

        B = magpy.getB(x1, (x, y, z))
        b_fin = 0
        for i in range(0, 3):
            b_fin += B[i]**2
        b_fin = np.sqrt( b_fin )
        b_fin *= 1000

        b.append( b_fin )

    fig, ax1 = plt.subplots()

    color = 'red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('magnetic intensity 1', color=color)
    ax1.plot(xa, bi, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('magnetic intensity 2', color=color)  # we already handled the x-label with ax1
    ax2.plot(xa, mgt, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.plot( xa, b, color='green' )

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    b.clear()


cnt = 0
end = False
for i in range( -30, 5 ):
    for j in range( -1, 21 ):
        for w in range( -2, 21 ):
            cnt += 1
            print( str(cnt) + ' ' + str( least ) + ' ' + str( mlx ) + ' ' + str(mly) + ' ' + str(mlz) + ' ' + str(rlx) + ' ' + str(rly) + ' ' + str(rlz) )
            main( mx, (i / 10) * 10**27, mz, (j / 10) * 10**9, (w / 10) * 10**9, rz )
            if cnt == 500:
                end = True
                break
        if end:
            break
    if end:
        break


printMinim()

print( mlx )
print( mly )
print( mlz )
print( rlx )
print( rly )
print( rlz )