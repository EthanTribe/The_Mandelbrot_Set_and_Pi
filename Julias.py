# Julia Set Generator v1


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



c = complex(-0.75,0.05)
R = abs((-1 - (1+4*abs(c))**0.5)/2)     # escape radius and quadratic formula

imax = 100 

# julia sequence length function
def inSet(x):                           
    iterate = x
    for i in range(imax):
        if abs(iterate) > R:
            return i              
        else:
            iterate = iterate**2 + c
    return imax

# values into the array
dim = 401
xList = np.linspace(-2,2,dim)
yList = np.linspace(-2,2,dim)
julia = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        pointIn = inSet(complex(xList[i],yList[j]))
        julia[j,i] = pointIn            

# plot the array
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')

cax = ax.matshow(julia,cmap=cm.magma_r,origin='lower',extent=(-2,2,-2,2))

# print the maximum value in the array if <imax Fatou set
print(np.amax(julia))   


#SEQUENCE
##plt.plot([-0.41653,1.41653],[0.300045,-0.300045],'b.')
#zn = [complex(1.06,-0.26)]#[complex(1.0625,-0.1575)]
#xs = []
#ys = []
##while abs(zn[-1]) <= R:
#for i in range(100):
#    xs += [zn[-1].real]
#    ys += [zn[-1].imag]
#    zn += [zn[-1]**2+c]
#plt.plot(xs,ys,'b.-',linewidth=0.5,markersize=0.5)

#plt.plot([-0.500312,1.500312],[0.0249922,-0.0249922],'b.')

plt.savefig('Julia.jpg',format='jpg',dpi=300)
plt.show()
