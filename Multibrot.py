# Julia Set Generator v1


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def inSet(c):                           # julia set formula
    iterate = 0
    for i in range(100):
        if abs(iterate) > 2:
            return i               # sqrt to exadertate the changes
        else:
            iterate = iterate**5 + c
    return i


xList = np.linspace(-2,2,1001)
yList = np.linspace(-2,2,1001)
julia = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        pointIn = inSet(complex(xList[i],yList[j]))
        julia[len(yList)-j-1,i] = pointIn                              # if the point is in the set mark it in the coordinate matrix


plt.imshow(julia,cmap=cm.magma)
plt.show()
    
