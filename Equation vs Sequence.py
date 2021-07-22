#--------------
# x_n vs. x(n)
#--------------

import numpy as np
import matplotlib.pyplot as plt

eps=0.00001

xns = np.array([-0.5])
xn = xns[-1]**2+xns[-1]+eps
while xn <= 100:    # just to make the plot extend further
    xns = np.concatenate((xns,np.array([xn])),axis=None)
    xn = xn**2+xn+eps

def x(n):
    return eps**0.5 * np.tan(eps**0.5 * (n) - np.pi/2)

ns = np.linspace(0,len(xns)-1,len(xns))
#xs = np.linspace(0,len(xns))
ys = np.array([x(n) for n in range(len(ns))])
axes = plt.gca()
axes.set_xlim([-10,len(ns)+10])
axes.set_ylim([-1.5,1.5])
#axes.set_aspect('equal')
#dif = xs[2]-xs[1]
#plt.plot(np.concatenate((xs,np.array([1.5+dif,1.5+2*dif])),axis=None),np.concatenate((ys,np.array([x(i) for i in [len(xs),len(xs)+1]])),axis=None),'-')
plt.plot(ns,ys,'-')
plt.plot(ns,xns,'.',markersize=2)
plt.xlabel('n')
plt.ylabel('x\u2099 / x(n)')
plt.legend(['x(n)','x\u2099'],loc='upper left')
plt.savefig('eqnvsseq.jpg',format='jpg',dpi=1200)
plt.show()
