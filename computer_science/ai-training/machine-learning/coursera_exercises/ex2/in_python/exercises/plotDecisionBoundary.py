from .plotData import plot
#import matplotlib.pyplot as plt
import numpy as np
def plotDB(X, y, theta):
    plt = plot(X, y)
    #plt.hold()
    # the decision boundary plot separates the positive
    # and negative samples, here the 
    # hypothesis is h_theta(x) = g(theta_Trns * x) 
    # the hypothesis function separates samples at h(x) = 0.5
    # for which the e^-(theta_trans * x) should be 1
    # for which theta_trans_* x = 0
    # i.e. theta_0 + theta_1 * x1 + theta2 * x2 = 0
    
    # Now get the two points on x1 and x2 to plot the line
    # two points can be max and min values of respective samples

    x1 = np.array([min(X[:, 0]), max(X[:, 0])])

    # Now x2 can be calculated , we have
    # theta_0 + theta_1 * x1 + theta_2 * x2 =0
    # theta_1 * x1 + theta_2 * x2 = -theta_0
    # theta_2 * x2 = -theta_0 -theta_1 * x1
    # x2 = - ( theta_0 + theta_1 * x1 ) * (1 / theta_2)
    x2 = - (1.0 / theta[2]) * ( theta[0] + theta[1] * x1)

    print(x1)
    print(x2)
    plt.plot(x1, x2)
    
    return plt