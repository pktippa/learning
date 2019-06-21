# On Regularization
import pandas as pd
import numpy as np
from exercises.plotData import plot
from exercises.mapFeature import featureMap
from exercises.costFunctionReg import getCost, getGrad
from exercises.plotDecisionBoundaryReg import plotDB
from exercises.advOptimizeReg import optimize
from exercises.predict import getPredictions

inp = pd.read_csv('../ex2data2.txt', header=None)

X_org = inp[inp.columns[0:2]].values
y_df = inp[2].values

m = len(y_df)

y = y_df.reshape((m, 1))

plt = plot(X_org, y)
# Labelling the markers
plt.legend(['y=1', 'y=0'])
# Labelling Axes
plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.show()

# Generating new features which are polynomial to try to fit the data points
x1 = X_org[:,0]
x1 = x1.reshape((m,1))
x2 = X_org[:,1]
x2 = x2.reshape((m, 1))
X = featureMap(x1, x2, m)
X_shape = X.shape
print('New features vector shape', X_shape)

initial_theta = np.zeros((X_shape[1], 1))
# Setting= regularization parameter lambda to 1
lambd = 1
cost, grad = getCost(initial_theta, X, y, lambd), getGrad(initial_theta, X, y, lambd)

print('Cost at initial theta (zeros): %f\n', cost)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros) - first five values only:\n')
print('\n', grad[0:5])
print('Expected gradients (approx) - first five values only:\n')
print(' 0.0085\n 0.0188\n 0.0001\n 0.0503\n 0.0115\n')

# Compute and display cost and gradient
# with all-ones theta and lambda = 10
test_theta = np.ones((X_shape[1], 1))
lambd = 10
cost, grad = getCost(test_theta, X, y, lambd), getGrad(test_theta, X, y, lambd)

print('Cost at initial theta (ones): %f\n', cost)
print('Expected cost (approx): 3.16\n')
print('Gradient at initial theta (ones) - first five values only:\n')
print('\n', grad[0:5])
print('Expected gradients (approx) - first five values only:\n')
print(' 0.3460\n 0.1614\n 0.1948\n 0.2269\n 0.0922\n')


theta = optimize(X, y, initial_theta)
print('Theta first 5 values after optimization\n')
print('\n', theta[0:5])

# Plotting the decision boundary
plt = plotDB(X_org, y, theta)
plt.show()

# Computing the accuracy
predictions = getPredictions(X, theta)

print('First 7 elements y : ', y[0:7])
print('First 7 elements predictions : ', predictions[0:7])

comparisons = ( y == predictions )

accuracy_ = np.zeros((X.shape[0], 1))
accuracy_[comparisons] = 1

print('Accuracy ', np.mean(accuracy_))