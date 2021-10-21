import numpy as np

def u_exact(t, I, w):
    return I*np.cos(w*t)