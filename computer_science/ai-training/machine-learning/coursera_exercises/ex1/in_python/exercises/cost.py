import numpy as np

def computeCost(X, y, theta):
    m = len(X)
    # Matrix multiplication of X and theta which is the hypothesis function
    hypothesis_X = np.matmul(X, theta)
    #print('shape', hypothesis_X.shape)
    # Calculating difference of hypothesis and y
    dif = hypothesis_X - y
    # print('shape', dif.shape)
    # Getting the Square of each individual element value
    # Element wise product - we can also use np.multiply(dif, dif)
    dif_sqr = dif * dif
    # Generating a row vector to multiply to get the sum of all the elements in the matrix
    #print('shape', dif_sqr.shape)
    ones = np.ones(m)
    #print('shape', ones.shape)
    # Multiplying row vector and difference square to get cost vector
    cost_mat = (0.5/m) * np.matmul(ones, dif_sqr)
    # Converting matrix 1 by 1 Ex: [5] to scalar value 5
    cost_scalar = np.asscalar(cost_mat)
    return cost_scalar