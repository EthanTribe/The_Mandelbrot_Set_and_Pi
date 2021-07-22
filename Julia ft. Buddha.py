import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# function to find N for a Julia sequence
def inSet(z,c):                          
    iterate = z 
    for i in range(100):
        if abs(iterate) > 2:
            return i               
        else:
            iterate = iterate**2 + c
    return i

# make the matrix for the background image
dim = 1001
xList = np.linspace(-2,2,dim)
yList = np.linspace(-2,2,dim)
julia = np.zeros((len(yList),len(xList)))
for i in range(len(xList)-1,-1,-1):
    for j in range(len(yList)):
        julia[j,i] = inSet(complex(xList[i],yList[j]),complex(-1.25-0.001**2,0.001))        

# plot the Julia/Fatou set in the background
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')

cax = ax.matshow(julia,cmap=cm.magma_r,origin='lower',extent=(-2,2,-2,2))


# function to find the next term in the sequence
def f(z,c):
    return z**2 + c

# e is the list of epsilons and p1 the first sequence with z_0 at the start of the parabola
e = np.linspace(0.001,0.021,400)
p1 = [complex(-1.25-e[0]**2,e[0])]

n = 400    # 2000 includes all points, last lists are NAN (not sure why)

# p is the list of lists of z_ns i.e. p[0] is the list of z_1s (z_1=c) p[1] the list of z_2s etc.
p = [p1]
while abs(p[-1][0]) <= 2:
    p += [[f(p[len(p)-1][0],p[0][0])]]

# add elements to the p[i]s for the sequences with c in e
while (abs(p[0][-1])<=2) and (len(p[0])<len(e)):
    p[0] += [complex(-1.25-e[len(p[0])]**2,e[len(p[0])])]
for i in range(len(p)-1):
    while (abs(p[i+1][-1])<=2) and (len(p[i+1])<len(p[i])):
        p[i+1] += [f(p[i][len(p[i+1])],p[0][len(p[i+1])])]

# plot the sequences
px = []
py = []
for i in range(n):
    px += [[pp.real for pp in p[i]]]
    py += [[pp.imag for pp in p[i]]]

colours = ['r','orange','g','b']
for i in range(n):
    plt.plot(px[i],py[i],color=colours[i%4],linestyle='None',marker='.',markersize=1)

plt.savefig('Julia.jpg',format='jpg',dpi=1200)
plt.show()
    
