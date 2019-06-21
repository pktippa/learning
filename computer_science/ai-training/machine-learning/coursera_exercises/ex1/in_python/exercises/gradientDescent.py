import numpy as np
from .cost import computeCost

def doGD(X, y, theta, alpha, num_iterations):
    J_history = np.zeros((num_iterations, 1))
    # number of training samples
    m = len(y)
    for itern in range(num_iterations):
        # theta = theta - alpha * (1/m) * SigSum(h(x) - y)X
        # X - shape - (97,2), theta - shape - (2,1)
        # Gives hypothesis shape (97,1)
        hypothesis = np.matmul(X, theta)
        #print('hypothesis shape', hypothesis.shape)
        # Diff shape is (97,1)
        dif = hypothesis - y
        #print('dif shape', dif.shape)
        # Now X_tranpose shape is (2,97)
        X_transpose = np.transpose(X)
        # Sigsum shape (2, 1)
        # Sigma sum is nothing but the Transpose matrix product with dif
        sigsum = np.matmul(X_transpose, dif)
        #print('sigsum shape', sigsum.shape)
        #print('X shape', X.shape)
        # alpha_sigsum
        alpha_sigsum = alpha * (1/m) * sigsum
        # Calculating final theta
        theta = theta - alpha_sigsum

        #print('theta ', theta)

        J_history[itern] = computeCost(X, y, theta)
    
    return theta, J_history