# Buddhabrot Subset Generator 


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



dim = 400
xList = np.linspace(-2,2,dim)
yList = np.linspace(-2,2,dim)
julia = np.zeros((len(yList),len(xList)))
diff = xList[1]-xList[0]

imax = 100

def inSet(c):                           # julia set formula
    zn = 0
    for i in range(imax):
        if abs(zn) > 2:
            return i               # sqrt to exadertate the changes
        else:
            zn = zn**2 + c
    return imax


def path(c):
    if inSet(c) != imax:
        zn = c                  # including zn=0 just makes that value dwarf everything else
        while abs(zn) <= 2:
            x = zn.real
            y = zn.imag
            #print(round(y/diff)+(dim-1)/2,round(x/diff)+(dim-1)/2)
            julia[int(round(y/diff)+(dim-1)/2)][int(round(x/diff)+(dim-1)/2)] += 1.0
            zn = zn**2 + c
        

cdim = 1000
a = 0.04
eps = []
for i in range(int(a*cdim**2)):
    eps += [a*np.random.random()+0.001]
eps.sort()
crands = [complex(-1.25-e**2,e) for e in eps]
for i in crands:
    path(i)
    #path(complex(-1.25-eps[100]**2,eps[100]))

plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')

cax = ax.matshow(julia**0.1,cmap=cm.gray,origin='lower',extent=(-2,2,-2,2))


#c = complex(-1.25-eps[3000]**2,eps[3000])
#zn = [c]
#xs,ys = [],[]
#while abs(zn[-1]) <= 2:
#    x = zn[-1].real
#    y = zn[-1].imag
#    diff = xList[1]-xList[0]
#    #print(round(y/diff)+(dim-1)/2,round(x/diff)+(dim-1)/2)
#    xs += [int(round(x/diff)+(dim-1)/2)] 
#    ys += [dim-1-int(round(y/diff)+(dim-1)/2)]
#    zn += [zn[-1]**2 + c]
#plt.plot(xs,ys,'y.-',linewidth=0.05,markersize=0.5)


plt.savefig('Buddhabrot.jpg',format='jpg',dpi=1200)
plt.show()


