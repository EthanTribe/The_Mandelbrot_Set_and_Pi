# Julia Set Generator v1


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def iterations(c):                           # julia set formula
    iterate = 0
    i=0
    while abs(iterate) < 2 and i < 10000:
        iterate = iterate**5 + c
        i += 1
    return i


##xList = np.linspace(0.25,1.25,4001)
##yList = np.linspace(-0.1,0.1,201)
##julia = np.zeros((len(yList),len(xList)))
##for i in range(len(xList)-1,-1,-1):
##    for j in range(len(yList)):
##        pointIn = inSet(complex(xList[i],yList[j]))
##        julia[len(yList)-j-1,i] = pointIn                              # if the point is in the set mark it in the coordinate matrix
##
##
##plt.imshow(julia,cmap=cm.magma)
##plt.show()


piList = [iterations(0.534995+10**-i) for i in range(10)]
print(piList)

# for point 0.53499... have sequence [2,5,18,57,...], seems promising.
# numerically find pinch points?
