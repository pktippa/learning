from .sigmoid import sigm
import numpy as np

def getPredictions(X, theta):
    p = np.zeros((X.shape[0], 1))
    condition = sigm(X.dot(theta)) >= 0.5
    p[condition] = 1

    return p