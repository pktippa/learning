from .plotData import plot
from .mapFeature import featureMap
#import matplotlib.pyplot as plt
import numpy as np
def plotDB(X, y, theta):
    # Performing the grid range
    u = np.linspace(-1, 1.5, 50)
    v = np.linspace(-1, 1.5, 50)

    z = np.zeros((u.shape[0], v.shape[0]))

    for i in range(u.shape[0]):
        for j in range(v.shape[0]):
            ft_map = featureMap(u[i].reshape(1,1), v[j].reshape(1,1), 1)
            z[i][j] =  ft_map.dot(theta)

    z = z.T
    plt = plot(X, y)

    plt.contour(u, v, z)
    
    return plt
    