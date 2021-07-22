# visulaises the sequence as a time series

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def c(p,q):
    mu = np.e**(2*np.pi*complex(0,1)*p/q)
    return 0.5*mu*(1-0.5*mu)



