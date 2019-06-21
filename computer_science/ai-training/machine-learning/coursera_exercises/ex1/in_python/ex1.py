from exercises import warmUpExercise
from exercises.plotData import plot 
from exercises.cost import computeCost
from exercises.gradientDescent import doGD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('Printing the Identitiy Matrix')

identitiy_matx = warmUpExercise.get5by5IdentityMatrix()
print(identitiy_matx)

inp = pd.read_csv('../ex1data1.txt', header=None)
X = inp[0].values
y = inp[1].values

# Calling plot in plotData.py file
#plot(X, y)
# Getting number of training examples
m = len(X)

# If we dont reshape the shape is getting as (97,) but not (97,1)
X = X.reshape((m,1))
y = y.reshape((m,1))

print('No of samples', m)
# Generating the column ones vector which is for theta_0 as X0
column_ones = np.ones((m, 1))

print(column_ones.shape, X.shape, y.shape)
# Now concatinating the ones column vector with feature matrix X
# Give axis=1 for concatinating column wise
X = np.concatenate((column_ones, X), axis=1)

# Iniatilizing theta vector with all zeros
theta = np.zeros((2, 1))

# Calling computeCost in cost.py file
calculatedCost = computeCost(X, y, theta)

print('Cost Calculated ', calculatedCost, ' vs the expected cost', 32.07)

# Further testing of cost function
theta = np.array([[-1],[2]])
calculatedCost = computeCost(X, y, theta)
print('Cost Calculated ', calculatedCost, ' vs the expected cost', 54.24)

# Gradient Descent Settings
iterations = 1500
alpha = 0.01

theta = np.zeros((2, 1))

theta, J_history = doGD(X, y, theta, alpha, iterations)

print('Theta found', theta)
print('Expected theta values (approx)\n')
print(' -3.6303\n  1.1664\n\n')

# Now plotting the hypothesis function
hypothesis = np.matmul(X, theta)
print('shape hypothesis', hypothesis.shape)
# Getting the second column from the X feature values by excluding the 1s column vector
# Note: but the shape is (97,) but no (97,1)
plt.plot(X[:,1], hypothesis)
# Calling the scatter plot to overlay the hypothesis line graph.
plot(X[:,1], y)