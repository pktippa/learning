import numpy as np
from .sigmoid import sigm

def getCost(theta, X, y, lambd=1):
    # Calculating matrix multiplication of X and theta
    X_x_theta = np.matmul(X, theta)
    # Getting the sigmoid values for calculating hypothesis function
    h_theta = sigm(X_x_theta)
    # Caluclating transpose of X which is used for calculating gradient
    X_trans = np.transpose(X)

    # Performing logarthmic operation on each element of matrix
    log_h_theta = np.log(h_theta)
    log_1_h_theta = np.log(1-h_theta)
    
    log_h_tht_trans = np.transpose(log_h_theta)
    log_1_h_tht_trans = np.transpose(log_1_h_theta)

    m = len(y)
    # Calculating Cost
    cost_J = (-1/m) * (np.matmul(log_h_tht_trans, y) + np.matmul(log_1_h_tht_trans, (1 - y)))

    # extra cost for regularization
    cost_reg = ( lambd / m ) * ( np.sum(theta ** 2) - np.asscalar(theta[0] ** 2) )

    # Combining both cost and regularization term
    total_cost = cost_J + cost_reg

    return total_cost

def getGrad(theta, X, y, lambd=1):

    m, n = X.shape
    theta = theta.reshape((n, 1))
    # Calculating matrix multiplication of X and theta
    X_x_theta = X.dot(theta)
    # Getting the sigmoid values for calculating hypothesis function
    h_theta = sigm(X_x_theta)
    #h_theta = h_theta.reshape((m,1))
    #print('Grad h_theta shape', h_theta.shape)
    #print('Y shape', y.shape)

    X_trans = np.transpose(X)

    #print('Grad X_trans shape', X_trans.shape)
    h_y_diff = h_theta - y
    #print('Grad h_y_diff shape', h_y_diff.shape)
    # Calculating Gradient.
    grad = (1/m) * X_trans.dot(h_y_diff)

    #print('Grad grad shape', grad.shape)
    # grad for regularization term
    funny_mat = np.eye(len(theta))
    funny_mat[0][0] = 0
    #print('funny mat shape', funny_mat.shape)
    grad_reg = (lambd / m) * (funny_mat.dot(theta))
    #grad_reg = grad_reg.reshape()
    # Combining gradients
    grad_total = grad + grad_reg
    #print('Grad Grad _tot shape', grad_total.shape)

    return grad_total