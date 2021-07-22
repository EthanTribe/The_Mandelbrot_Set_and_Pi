# visulaises the sequence as a time series

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


c = complex(-1.25,0)

def f(z):
    return z**2+c

zs = [0]

N = 10000004
for i in range(N):
    zs += [f(zs[-1])]

print(zs[-8:])
