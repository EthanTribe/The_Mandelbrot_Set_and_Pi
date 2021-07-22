# Julia Set Generator v1


import numpy as np
import matplotlib.pyplot as plt


gR = 0.5*(1+5**0.5)                     # the golden ratio
c = complex(1,0)                       # -0.8,0.156 1-gR,0 -0.75,0 0.25,0 -0.15,0.65 0.06,0.63
R = abs((-1 - (1+4*abs(c))**0.5)/2)     # escape radius and quadratic formula


def inSet(x,iMax):                           # julia set formula
    iterate = x
    for i in range(iMax):
        if abs(iterate) > R:
            return 0               
        else:
            iterate = iterate**2 + c
    return 1


def computeArea(iMax,x1,x2,y1,y2,xn=1000):
    yn = ((y2-y1)/(x2-x1))*xn
    xList = np.linspace(x1,x2,xn)
    yList = np.linspace(y1,y2,yn)
    area = 0
    for i in range(len(xList)-1,-1,-1):
        for j in range(len(yList)):
            pointIn = inSet(complex(xList[i],yList[j]),iMax)
            area += pointIn                                     # if the point is in the set add it to the area
    return area*((x2-x1)/xn)**2 

##x2 = [2]+[1 for i in range(19)]
##xn = [1000,1000,1500,2000,2500,3000,3500] + [4000 for i in range(13)]
##result = [computeArea(i+1,-x2[i],x2[i],-2,2,xn[i]) for i in range(20)]
##print(result)

result = [8.208768, 4.5492479999999995, 2.0588444444444445, 0.75984, 0.26664448, 0.09420444444444444, 0.033639183673469394, 0.012069, 0.004340999999999999, 0.0015429999999999999, 0.000552, 0.000206, 6.5e-05, 2.4999999999999998e-05, 9.999999999999999e-06, 3e-06, 1e-06, 0.0, 0.0, 0.0]

differences = []
for i in range(16):
    differences += [result[i]/result[i+1]]
print(differences,"\n")                     # not to dissimilar

plt.plot(differences,'-')
##plt.xscale('log')
plt.show()                                  # log???, fp error at the end
