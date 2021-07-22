# Mandelbrot sequence length


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def iterations(c):                           # julia set formula
    iterate = 0
    i=0
    while abs(iterate) <= 2 and i < 1000000000:
        iterate = iterate**2 + c
        i += 1
    return i

for i in range(10):
    print(iterations(complex(-1.25-2*100**-i,10**-i)))
piList = [iterations(complex(-1.25-100**-i,10**-i)) for i in range(10)]
print(piList)
    
