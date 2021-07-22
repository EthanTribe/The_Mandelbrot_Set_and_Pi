import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def inSet(c):                           # julia set formula
    zn = 0
    for i in range(1000000):
        if abs(zn) > 2:
            return i               # sqrt to exadertate the changes
        else:
            zn = zn**2 + c
    return i

path = [2*inSet(complex(-1.25-10**(-i*2),10**-i)) for i in range(10)] #*10**(-0.5*i)
print(path)
