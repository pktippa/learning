import numpy as np
def featureMap(x1, x2, m):
    degree = 6
    out = np.ones((m, 1))

    # Example for instance of features for only power of 3
    # x1^3, x1^2 * x2, x1 * x2^2, x2^3
    # We can see that powers x1 decreases from 3 to 0,
    # powers of x2 increases from 0 to 3
    # So first loop increases from 1 to degree
    # second loop increases from 0 to counter of first loop
    for i in range(1, degree+1):
        for j in range(i+1):
            new_feature_vec = (x1 ** (i-j)) * (x2 ** j)
            out = np.concatenate((out, new_feature_vec), axis=1)
    
    return out