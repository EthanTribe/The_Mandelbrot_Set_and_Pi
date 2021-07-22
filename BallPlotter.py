# Ball plotter

import numpy as np
import matplotlib.pyplot as plt


N = 0.5

# setting up the graph and axis
fig,ax = plt.subplots(1,1)
ax.set_aspect('equal')

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])

# plotting the conservation of energy circle
energyx = np.concatenate((np.linspace(-1.0,-0.9,30),np.linspace(-0.9,0.9,40),np.linspace(0.9,1.0,30)))
energyy = np.array([(1-energyx[i]**2)**0.5 for i in range(len(energyx))])
plt.plot(energyx, energyy,'-b')
plt.plot(energyx, -energyy,'-b')

# calculating the velocities
u = np.array([0])   # y coords
v = np.array([-1])  # x coords

c = u[-1] + 10**N*v[-1]
vv = (10**N*c+(-c**2+100**N+1)**0.5)/(1+100**N)
uu = -10**N*vv + c
u = np.concatenate((u,np.array([uu,-uu])))
v = np.concatenate((v,np.array([vv,vv])))
    
while u[-1]>0:   #(0<=u[-1]<=v[-1]) == False
    c = u[-1] + 10**N*v[-1]
    vv = (10**N*c+(-c**2+100**N+1)**0.5)/(1+100**N)
    uu = -10**N*vv + c
    u = np.concatenate((u,np.array([uu,-uu])))
    v = np.concatenate((v,np.array([vv,vv])))

v = v[:-1]          # last u was +ve so couldn't have hit wall --> remove last pair
u = u[:-1]          

print(len(v)-1)     # counting lines not points, hence length -1

# plotting the coordinates and paths
plt.plot(v,u,'deeppink')    
plt.plot(v,u,'r.')

# plotting the end condition
x1 = 10**N/(1+100**N)**0.5
plt.plot([0,x1],[0,x1*10**-N],'g-')     
    
plt.show()
