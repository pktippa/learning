import matplotlib.pyplot as plt
import numpy as np

def plot(X, y):
    positive_indices = np.where(y == 1)
    negative_indices = np.where(y == 0)
    # Number of samples
    m = len(X)
    #print('X', X)
    X1_pos = X[:,0]
    X1_pos = X1_pos.reshape((m, 1))
    X1_pos = X1_pos[positive_indices]
    X2_pos = X[:, 1]
    X2_pos = X2_pos.reshape((m, 1))
    X2_pos = X2_pos[positive_indices]
    plt.scatter(X1_pos, X2_pos, c='b',marker='+')

    X1_neg = X[:,0]
    X1_neg = X1_neg.reshape((m, 1))
    X1_neg = X1_neg[negative_indices]
    X2_neg = X[:, 1]
    X2_neg = X2_neg.reshape((m, 1))
    X2_neg = X2_neg[negative_indices]
    plt.scatter(X1_neg, X2_neg, c='y', marker='o')

    return plt