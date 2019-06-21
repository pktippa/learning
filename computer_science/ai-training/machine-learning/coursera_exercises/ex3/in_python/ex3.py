import numpy as np

# Importing from ex2 regularization cost function
from exercises.costFunctionReg import getCost, getGrad
from exercises.oneVsAll import oneva
from exercises.predictOneVsAll import predict as prdova

# Test case for lrCostFunction
print('\nTesting lrCostFunction() with regularization')

theta_t = np.array([[-2], [-1], [1], [2]])
X_arange = np.arange(1,16).reshape(3,5)
X_t = X_arange.T
X_t = (1/10) * X_t
column_ones = np.ones((5, 1))
X_t = np.concatenate((column_ones, X_t), axis=1)
y_t = np.array([[1],[0],[1],[0],[1]])
lambda_t = 3
J, grad = getCost(theta_t, X_t, y_t, lambda_t), getGrad(theta_t, X_t, y_t, lambda_t)

print('\nCost:', J,  '\n')
print('Expected cost: 2.534819\n')
print('Gradients:\n')
print(grad, '\n')
print('Expected gradients:\n')
print(' 0.146561\n -0.548558\n 0.724722\n 1.398003\n')

X_org = np.genfromtxt('../X_input.csv', delimiter=',')
y_org = np.genfromtxt('../y_output.csv', delimiter=',')

y_org = y_org.reshape((len(y_org), 1))
print('X shape ', X_org.shape, 'el', X_org[0][0])
print('y shape ', y_org.shape, 'el', y_org[0])

num_labels = 10
lambd = 0.1

all_theta = oneva(X_org, y_org, num_labels, lambd)

p = prdova(all_theta, X_org)

print('shape of predictions ', p.shape)
print('printing first value to see', p[0])
p = p.reshape((len(p), 1))
comparisons = (p == y_org)

accuracy_ = np.zeros((len(y_org),1))
accuracy_[comparisons] = 1

print('Accuracy with oneVsAll method', np.mean(accuracy_))