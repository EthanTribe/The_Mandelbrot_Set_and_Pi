# Julia Set Generator v2?


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



dim = 31
rec = np.linspace(-2,1,dim)
imc = np.linspace(-1.5,1.5,dim)
inddim = 51


fig,axs = plt.subplots(dim,dim,gridspec_kw={'hspace':0,'wspace':-0.915})
for i in range(dim):
    for j in range(dim):            
        imageversion = i+1
        gR = 0.5*(1+5**0.5)                     # the golden ratio
        c = complex(rec[j],imc[dim-1-i])        # going from right to left and top to bottom
        R = (1 + (1+4*abs(c))**0.5)/2           # escape radius and quadratic formula

        def inSet(x):                           # julia set formula
            iterate = x
            for k in range(100):
                if abs(iterate) > R:
                    return k               
                else:
                    iterate = iterate**2 + c
            return (k+1)

        xmin, xmax = -2,2
        ymin, ymax = -2,2
        xdim, ydim = inddim,inddim
        xList = np.linspace(xmin,xmax,xdim)
        yList = np.linspace(ymin,ymax,ydim)
        julia = np.zeros((len(yList),len(xList)))
        for a in range(len(xList)-1,-1,-1):
            for b in range(len(yList)):
                pointIn = inSet(complex(xList[a],yList[b]))
                julia[len(yList)-b-1,a] = pointIn

        
        #plt.ion()
##        ax=fig.add_subplot(i+1,j+1,dim**2)
##        ax.set_xlim(xmin,xmax)
##        ax.set_ylim(ymin,ymax)
##        ax.set_aspect('equal')
        ax = axs[i,j]
        ax.matshow(julia**0.5,cmap=cm.magma)
        ax.axis('off')
    print(i)

#plt.savefig('Julia2 Mbrot.jpg',format='jpg',dpi=1200)
plt.show()

        #cax = ax.matshow(julia,cmap=cm.magma,origin='lower',extent=(xmin,xmax,ymin,ymax),vmin=-0.5*np.pi,vmax=9.5*np.pi)

        #plt.imsave('savedmbrot.jpg',julia)
        #fig.savefig('savedmbrot.eps', format='eps', dpi=1200)
        #fig.savefig('mbrot{}.jpg'.format(imageversion), format='jpg', dpi=1200)

        

##  STAIRS
##    plt.subplot(1,1,1)
##    plt.xticks([0,np.pi,2*np.pi,3*np.pi,4*np.pi,5*np.pi])
##    plt.yticks([])
##    points = stairs(julia)
##    plt.plot(points,np.linspace(0,100,len(points)),'-',linewidth=0.5)
##plt.savefig('stairs{}.jpg'.format(imageversion),format='jpg',dpi=1200)
##    #plt.show()

