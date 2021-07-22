import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


imax = 1000
def inSet(c):                           # julia set formula
    iterate = 0 #complex(0.5,0.5)
    for i in range(imax):
        if abs(iterate) > 2:
            return i               # sqrt to exadertate the changes
        else:
            iterate = iterate**2 + c
    return imax

dim = 401
xmin,xmax = -1.45,-1.05#-1.27,-1.23
ymin,ymax = -0.1,0.3
xList = np.linspace(xmin,xmax,dim)
yList = np.linspace(ymin,ymax,dim)
points = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        pointIn = inSet(complex(xList[i],yList[j]))
        points[j,i] = pointIn                              # if the point is in the set mark it in the coordinate matrix

plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_aspect('equal')

power = 1
cax = ax.matshow(points**power,cmap=cm.magma_r,origin='lower',extent=(xmin,xmax,ymin,ymax),vmax=imax**power)

xs = [-1.25-2*(0.001*i)**2 for i in range(200)]
ys = [0.001*i for i in range(200)]
plt.plot(xs,ys,'b.-',linewidth=0.5,markersize=0.5)

plt.savefig('Mbrot.jpg',format='jpg',dpi=300)
plt.show()
    
