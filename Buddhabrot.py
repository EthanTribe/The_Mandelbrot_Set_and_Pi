# Buddhabrot and Anti-Buddhabrot Generator


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# array set-up
dim = 401
xList = np.linspace(-2,2,dim)
yList = np.linspace(-2,2,dim)
julia = np.zeros((len(yList),len(xList)))
diff = xList[1]-xList[0]

imax = 100

# mbrot function which returns N and the sequence
def inSet(c):                           
    zn = [0]
    for i in range(imax):
        if abs(zn[-1]) > 2:
            return i,zn
        else:
            zn += [zn[-1]**2 + c]
    return imax,zn

# the function to incriment the array for each term in the sequence for c
def path(c):
    i,zn = inSet(c)
    if i != imax:
        for z in zn[1:-1]:  # no z_0=0 since it is in every sequence and no last term since it has modulus >2
            x = z.real
            y = z.imag
            julia[int(round(y/diff)+(dim-1)/2)][int(round(x/diff)+(dim-1)/2)] += 1.0

# the function for the anti-buddhabrot
def antipath(c):
    i,zn = inSet(c)
    if i == imax:
        for z in zn[1:-1]:
            x = z.real
            y = z.imag
            julia[int(round(y/diff)+(dim-1)/2)][int(round(x/diff)+(dim-1)/2)] += 1.0
            
# generating the paths for random c
cdim = 4000
crands = [complex(4*np.random.random()-2,4*np.random.random()-2) for i in range(cdim**2)]
for i in crands:
    path(i)         # change for antipath(i) to make the anti-buddhabrot

plt.imshow(julia,cmap=cm.gray)  # need julia**0.5 for anti to exaggerate image
    
plt.savefig('Buddhabrot.jpg',format='jpg',dpi=300)
plt.show()


