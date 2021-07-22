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
    imageversion = i+1
    gR = 0.5*(1+5**0.5)                     # the golden ratio
    eps = 0.05    #1/(1000+20.5*i)
    c = complex(-0.75,eps)    # 0.33+eps,0.39191835884530846
    R = abs((1 + (1+4*abs(c))**0.5)/2)     # escape radius and quadratic formula
    #R = abs((1 + (-1-4*abs(c))**0.5)/2) what?!


    def inSet(x):                           # julia set formula
        iterate = x
        for i in range(2500):
            if abs(iterate) > R:
                return i               
            else:
                iterate = iterate**2 + c
        return (i+1)

    xmin, xmax = -2,2 #-1.1,1.1
    ymin, ymax = -2,2
    xdim,ydim = 500,500
    xList = np.linspace(xmin,xmax,xdim)
    yList = np.linspace(ymin,ymax,ydim)
    julia = np.zeros((len(yList),len(xList)))
    for i in range(len(xList)-1,-1,-1):
        for j in range(len(yList)):
            pointIn = eps*inSet(complex(xList[i],yList[j]))
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
    
    def eqn(z):
        return z**2+c
    z0 = complex(0.35,0.15)      # starting point
    xs = [z0.real]
    ys = [z0.imag]
    for i in range(int(inSet(complex(xs[0],ys[0])))):    # the perfect number
        z0 = eqn(z0)
        xs += [z0.real]
        ys += [z0.imag]
    plt.plot(xs,ys,'k.',linewidth=0.5,markersize=0.5)
    plt.plot([xs[0]],[ys[0]],color='purple',marker=r'$\bigodot$',markersize=10)       # colour to match starting region
    
    #plt.imsave('savedmbrot.jpg',julia)
    #fig.savefig('savedmbrot.eps', format='eps', dpi=1200)
    fig.savefig('julia{}.jpg'.format(imageversion), format='jpg', dpi=300)
    

##  STAIRS
##    plt.subplot(1,1,1)
##    plt.xticks(np.arange(0,12*np.pi,step=np.pi),('0','$\pi$','2$\pi$','3$\pi$','4$\pi$','5$\pi$','6$\pi$','7$\pi$','8$\pi$','9$\pi$','10$\pi$','11$\pi$'))
##    plt.yticks(np.arange(0,110,step=10),('0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'))
##    points = stairs(julia)
##    plt.plot(points,np.linspace(0,100,len(points)),'-',linewidth=0.5,label='$\epsilon$={}'.format(eps))
##plt.legend()
##plt.savefig('stairs{}.jpg'.format(imageversion),format='jpg',dpi=1200)
##    #plt.show()


