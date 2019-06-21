import numpy as np
from .advOptimizeReg import optimize

def oneva(X, y, num_labels, lambd):
    # m = number of samples
    # n = number of features
    m, n =  X.shape
    all_theta = np.zeros((n+1, num_labels))
    # Adding bias column ones vector
    X = np.concatenate((np.ones((m, 1)), X), axis=1)
    # Looping through number of label
    # for each label generating the label y vector having value of the iteration value
    for i in range(1, num_labels + 1 ):
        theta = all_theta[:, i-1]
        y_ = np.zeros((m,1))
        y_[ y == i ] = 1
        all_theta[:, i-1] = optimize(X, y_, theta)

    return all_theta

