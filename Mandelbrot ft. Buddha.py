import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def inSet(c):                           # julia set formula
    iterate = 0 #complex(0.5,0.5)
    for i in range(100):
        if abs(iterate) > 2:
            return i               # sqrt to exadertate the changes
        else:
            iterate = iterate**2 + c
    return i

dim = 1001
xList = np.linspace(-2,2,dim)
yList = np.linspace(-2,2,dim)
mbrot = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        mbrot[len(yList)-j-1,i] = inSet(complex(xList[i],yList[j]))                              # if the point is in the set mark it in the coordinate matrix


plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')

cax = ax.matshow(mbrot**0.5,cmap=cm.magma_r,origin='lower',extent=(-2,2,-2,2))




def f(z,c):
    return z**2 + c
e = np.linspace(0.001,1.001,1000)
p1 = [complex(-1.25-e[0]**2,e[0])]

n = 20

p = [p1]
for i in range(n-1):
    p += [[f(p[len(p)-1][0],p[0][0])]]

while abs(p[0][-1]) <= 2:
    p[0] += [complex(-1.25-e[len(p[0])]**2,e[len(p[0])])]
for i in range(n-1):
    while abs(p[i+1][-1]) <= 2:
        p[i+1] += [f(p[i][len(p[i+1])],p[0][len(p[i+1])])]
#for i in range(n):
    #p[i].pop()          # removing the term over 2


px = []
py = []
for i in range(n):
    px += [[pp.real for pp in p[i]]]
    py += [[pp.imag for pp in p[i]]]

colours = ['r','orange','g','b','purple']
#for i in range(n):
#    plt.plot(px[i],py[i],color=colours[i//4],linestyle='-',linewidth=0.5)

fixed = [complex(-0.65,0)]
for i in range(100):
    fixed += [f(fixed[-1],fixed[0])]
fixedx = [z.real for z in fixed]
fixedy = [z.imag for z in fixed]
plt.plot(fixedx,fixedy,'b.',markersize=0.1)

plt.savefig('Mbrot.jpg',format='jpg',dpi=1200)
plt.show()
    
