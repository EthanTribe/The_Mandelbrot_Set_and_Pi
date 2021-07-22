# visulaises the sequence as a time series

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


c = -1.9

def f(z):
    return z**2+c

zs = [0]

N = 50
for i in range(N):
    zs += [f(zs[-1])]


fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(0,N)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
ax.set_xlabel('n')
ax.set_ylabel('z\u2099',rotation=0)

plt.plot([i for i in range(N+1)],zs,'k.-',markersize=3,linewidth=1)
plt.savefig('Squigle.jpg',format='jpg',dpi=300)
plt.show()
