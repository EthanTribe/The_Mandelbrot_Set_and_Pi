# Julia Set Generator v2?


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# the function to convert the matrix into a sorted list
def stairs(mat):
    x = np.sort(mat,axis=None)
    return x[100000:-1000]  # removing the excess of points at the ends

# the loop to make different staircases
for i in range(4):
    imageversion = i+1
    eps = 2**(-i-1)
    c = complex(-0.75,eps)
    R = abs((1 + (1+4*abs(c))**0.5)/2)

    # function to find N
    def inSet(x):                       
        iterate = x
        for i in range(1000):
            if abs(iterate) > R:
                return i               
            else:
                iterate = iterate**2 + c
        return (i+1)

    # generating the matrix
    xmin, xmax = -2,2
    ymin, ymax = -2,2
    xdim,ydim = 500,500
    xList = np.linspace(xmin,xmax,xdim)
    yList = np.linspace(ymin,ymax,ydim)
    julia = np.zeros((len(yList),len(xList)))
    for i in range(len(xList)-1,-1,-1):
        for j in range(len(yList)):
            pointIn = eps*inSet(complex(xList[i],yList[j]))     # multiply N by power of eps
            julia[len(yList)-j-1,i] = pointIn                              

    # convert the matrix into a list
    points = stairs(julia)
    print(len(points))
    
    colours = ['r','orange','g','b','purple']
    ci = imageversion-1
    
    # plot the sorted list as index against element
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel('Value')
    ax.set_ylabel('Index (1000s)',rotation=90)
    ax.set_xticks(np.arange(0,18*np.pi,step=np.pi))
    ax.set_xticklabels(['0','$\pi$','2$\pi$','3$\pi$','4$\pi$','5$\pi$','6$\pi$','7$\pi$','8$\pi$','9$\pi$','10$\pi$','11$\pi$','12$\pi$','13$\pi$','14$\pi$','15$\pi$','16$\pi$','17$\pi$'])
    plt.plot(points,np.linspace(0,(len(points)-1)/1000,len(points)),color=colours[ci%5],linestyle='-',marker='None',linewidth=0.5,label='$\epsilon$={}'.format(eps))
    plt.legend()
plt.savefig('stairs{}.jpg'.format(eps),format='jpg',dpi=300)



