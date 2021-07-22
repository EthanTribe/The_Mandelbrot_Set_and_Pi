import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


imax = 1000

# define the function to iterate the Mbrot sequence
def inSet(c):                           
    iterate = 0
    for i in range(imax):
        if abs(iterate) > 2:
            return i
        else:
            iterate = iterate**2 + c
    return imax

# set-up the array representing the complex plane
dim = 1001
xmin,xmax = -2,1
ymin,ymax = -1.5,1.5
xList = np.linspace(xmin,xmax,dim)
yList = np.linspace(ymin,ymax,dim)
points = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        pointIn = inSet(complex(xList[i],yList[j]))
        points[j,i] = pointIn

plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_aspect('equal')

power = 0.5
cax = ax.matshow(points**power,cmap=cm.magma_r,origin='lower',extent=(xmin,xmax,ymin,ymax))
plt.savefig('Mbrot.jpg',format='jpg',dpi=300)
plt.show()
    
