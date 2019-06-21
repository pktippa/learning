import numpy as np
from .sigmoid import sigm
def predict(all_theta, X):
    X = np.concatenate((np.ones((X.shape[0], 1)), X) , axis=1)
    z = X.dot(all_theta)
    h = sigm(z)

    p = np.argmax(h, axis=1).T
    # Since it is zero indexed
    p = p + 1

    return p
