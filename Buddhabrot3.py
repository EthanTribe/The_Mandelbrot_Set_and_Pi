# Buddhabrot Subset Generator with the last k points highlighted


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



for k in range(1):
    imversion = k
    
    dim = 4000   # works with even still have odd to test
    xList = np.linspace(-2,2,dim+1)
    yList = np.linspace(-2,2,dim+1)
    mbrot = np.zeros((dim,dim))
    diff = xList[1]-xList[0]
    
    imax = 100
    
    def inSet(c):                           # mbrot set formula
        zn = 0
        for i in range(imax):
            if abs(zn) > 2:
                return i
            else:
                zn = zn**2 + c
        return imax
    
    
    def path(c):
        if inSet(c) != imax:
            zn = c                  # including zn=0 just makes that value dwarf everything else
            while abs(zn) <= 2:
                x = zn.real
                y = zn.imag
                mbrot[int(round(y/diff-0.5)+int(dim/2))][int(round(x/diff-0.5)+int(dim/2))] += 1.0
                zn = zn**2 + c
            
    
    cdim = 4000
    
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
    

    cax = ax.matshow(mbrot**0.1,cmap=cm.gray,origin='lower',extent=(-2,2,-2,2))
    
    
#    lengths = []
#    for i in range(len(eps)):
#        zs = [crands[i]]
#        xs,ys = [],[]
#        while abs(zs[-1]) <= 2:
#            xs += [zs[-1].real]
#            ys += [zs[-1].imag]
#            zs += [zs[-1]**2 + crands[i]]
#        firstoflasts = max([0,len(zs)-imversion])
#        plt.plot(xs[firstoflasts:],ys[firstoflasts:],'y.',linewidth=0.05,markersize=0.5)
#        lengths += [len(zs)]
#    print(max(lengths))        
    
    plt.savefig('Buddhabrot{}.jpg'.format(imversion),format='jpg',dpi=1200)
    plt.show()


