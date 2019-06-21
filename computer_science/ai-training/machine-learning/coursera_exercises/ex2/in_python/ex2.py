from exercises.plotData import plot
from exercises.costFunction import getCost
from exercises.advOptimize import optimize
from exercises.plotDecisionBoundary import plotDB
import pandas as pd
import numpy as np

inp = pd.read_csv('../ex2data1.txt', header=None)

X_org = inp[inp.columns[0:2]].values
# Giving directly the index of column for dataframe
y_df = inp[2].values
# Number of training samples
m = len(y_df)
# Reshaping from (100,) to (100,1)
y = y_df.reshape((m, 1))

# Plotting data
plt = plot(X_org, y)
# Labelling the markers
plt.legend(['Admitted', 'Not Admitted'])
# Labelling Axes
plt.xlabel('Exam 1 Score')
plt.ylabel('Exam 2 Score')
plt.show()

(m, n) = X_org.shape

# the intercept vector
column_ones = np.ones((m, 1))
# Adding the intercept one's for theta0
X = np.concatenate((column_ones, X_org), axis=1)


initial_theta = np.zeros((n+1, 1))
(cost_J, gradient) = getCost(X, y, initial_theta)

print('Cost at initial theta (zeros):\n', cost_J)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros): \n')
print(gradient)
print('Expected gradients (approx):\n -0.1000\n -12.0092\n -11.2628\n')

# For advanced optimization or finding the parameters automatically
# see advOptimize.py
theta = optimize(X, y, initial_theta)
# After advOptimize the expected values
#print('Cost at theta found by optimize:', res)
#print('Expected cost (approx): 0.203\n')
print('theta: \n')
print('\n', theta)
print('Expected theta (approx):\n')
print(' -25.161\n 0.206\n 0.201\n')

print('theta_shape', theta.shape)

# Plot Decision boundary
pltDb = plotDB(X_org, y, theta)
pltDb.show()