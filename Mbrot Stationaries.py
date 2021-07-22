# Julia Set Generator v2?


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



for i in range(6):
    imageversion = i
    #c = complex(-1.25,0)



    def inSet(c):                           # mbrot set formula
        iterate = 0
        for i in range(100):
            if abs(iterate) > 2:
                return i               
            else:
                iterate = iterate**2 + c
        return (i+1)

    xmin, xmax = -2,2
    ymin, ymax = -2,2
    xdim,ydim = 100,100
    xList = np.linspace(xmin,xmax,xdim)
    yList = np.linspace(ymin,ymax,ydim)
    julia = np.zeros((len(yList),len(xList)))
    for i in range(len(xList)-1,-1,-1):
        for j in range(len(yList)):
            julia[len(yList)-j-1,i] = inSet(complex(xList[i],yList[j]))                              # if the point is in the set mark it in the coordinate matrix

    
    plt.ion()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.set_aspect('equal')

    cax = ax.matshow(julia,cmap=cm.magma_r,origin='lower',extent=(xmin,xmax,ymin,ymax))

    zpoly = np.array([1,0,-1.25])
    def f(zp):
        new = np.convolve(zp,zp)
        new[-1] += 1.25
        return new
    for n in range(imageversion):      
        zpoly = f(zpoly)
        print(n)
    zpoly[-2] -= 1.0
    zroots = np.roots(zpoly)
    plt.plot([x.real for x in zroots],[x.imag for x in zroots],'b.')
    
    
    #plt.imsave('savedmbrot.jpg',julia)
    #fig.savefig('savedmbrot.eps', format='eps', dpi=1200)
    fig.savefig('mbrotstationaries{}.jpg'.format(imageversion), format='jpg', dpi=1200)
    




