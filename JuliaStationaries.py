# Julia Set Generator v2?


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def stairs(mat):
    x = np.sort(mat,axis=None)
    while x[0] == 0:
        x = np.delete(x,0)
    return x


for i in range(1):
    imageversion = i
    gR = 0.5*(1+5**0.5)                     # the golden ratio
    eps = 10**(-3)
    c = complex(0.25+eps,0)    # 0.33+eps,0.39191835884530846
    R = abs((1 + (1+4*abs(c))**0.5)/2)     # escape radius and quadratic formula
    #R = abs((1 + (-1-4*abs(c))**0.5)/2) what?!


    def inSet(x):                           # julia set formula
        iterate = x
        for i in range(1000):
            if abs(iterate) > R:
                return i               
            else:
                iterate = iterate**2 + c
        return (i+1)

    xmin, xmax = -1.1,1.1 #0.325,0.625
    ymin, ymax = -1.1,1.1 #0.0,0.3
    xdim,ydim = 500,500
    xList = np.linspace(xmin,xmax,xdim)
    yList = np.linspace(ymin,ymax,ydim)
    julia = np.zeros((len(yList),len(xList)))
    for i in range(len(xList)-1,-1,-1):
        for j in range(len(yList)):
            pointIn = eps**0.5*inSet(complex(xList[i],yList[j]))
            julia[len(yList)-j-1,i] = pointIn                              # if the point is in the set mark it in the coordinate matrix

    
    plt.ion()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.set_aspect('equal')

    cax = ax.matshow(julia,cmap=cm.tab10,origin='lower',extent=(xmin,xmax,ymin,ymax),vmin=-0.5*np.pi,vmax=9.5*np.pi)
    cbar = fig.colorbar(cax,ticks=np.arange(0,10*np.pi,step=np.pi))
    cbar.ax.set_yticklabels(('0','$\pi$','2$\pi$','3$\pi$','4$\pi$','5$\pi$','6$\pi$','7$\pi$','8$\pi$','9$\pi$'))

    zpoly = np.array([1,0,c])
    def f(zp):
        new = np.convolve(zp,zp)
        new[-1] += c
        return new
    for n in range(imageversion):      # different past 6, errors after 10
        zpoly = f(zpoly)
        print(n)
    zpoly[-2] -= 1.0
    zroots = np.roots(zpoly)
    plt.plot([x.real for x in zroots],[x.imag for x in zroots],'k.')
    
    
    #plt.imsave('savedmbrot.jpg',julia)
    #fig.savefig('savedmbrot.eps', format='eps', dpi=1200)
    fig.savefig('juliastationaries{}.jpg'.format(imageversion), format='jpg', dpi=1200)
    




