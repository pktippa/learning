import numpy as np

def rand(m, n):
    
    epsolon = 0.12

    return ( ( np.random.rand(m, 1 + n) * 2 * epsolon ) - epsolon )