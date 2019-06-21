import numpy as np
from exercises.nnCostFunction import getCost
from exercises.sigmoid import sigmoidGradient
from exercises.randomInitialize import rand

input_layer_size  = 400  # 20x20 Input Images of Digits
hidden_layer_size = 25   # 25 hidden units
num_labels = 10          # 10 labels, from 1 to 10   
                          # (note that we have mapped "0" to label 10)
# =========== Part 1: Loading data ===============

X_org = np.genfromtxt('../../ex3/X_input.csv', delimiter=',')
y_org = np.genfromtxt('../../ex3/y_output.csv', delimiter=',')

y_org = y_org.reshape((len(y_org), 1))

m, n = X_org.shape

print('X_org shape', X_org.shape)
print('y_org shape', y_org.shape)

# ================ Part 2: Loading Parameters ================

Theta1 = np.genfromtxt('../data/Theta1.csv', delimiter=',')
print('Loaded Theta1 shape', Theta1.shape)

Theta2 = np.genfromtxt('../data/Theta2.csv', delimiter=',')
print('Loaded Theta2 shape', Theta2.shape)

# unrolling parameters
# First transpose, then normal flatten
tmpTheta1 = Theta1.flatten()
tmpTheta1 = tmpTheta1.reshape((len(tmpTheta1), 1))
print('Unrolling Theta1 shape', tmpTheta1.shape)

tmpTheta2 = Theta2.flatten()
tmpTheta2 = tmpTheta2.reshape((len(tmpTheta2), 1))
print('Unrolling Theta2 shape', tmpTheta2.shape)

nn_params = np.concatenate((tmpTheta1, tmpTheta2), axis=0)

# ================ Part 3: Compute Cost (Feedforward) ================
'''
lambd = 0
theta1 = np.arange(1,7).reshape((2, 3))
print('Original t1', theta1)
theta2 = np.arange(1,13).reshape((4, 3))
print('original t2', theta2)
tmpTheta1 = theta1.flatten()
tmpTheta1 = tmpTheta1.reshape((len(tmpTheta1), 1))

tmpTheta2 = theta2.flatten()
tmpTheta2 = tmpTheta2.reshape((len(tmpTheta2), 1))
nn_params = np.concatenate((tmpTheta1, tmpTheta2), axis=0)
cost = getCost(nn_params, 2, 2, 4, 1, 1, lambd)
'''
lambd = 0 # With out regularization
#print('nn_params 656', nn_params[655], '')
cost = getCost(np.copy(nn_params), input_layer_size, hidden_layer_size, num_labels, X_org, y_org, lambd)
print('Cost at parameters (loaded from ex4weights):', cost, ' value should be 0.287629')

# Implementing Regularization
print('\nChecking Cost Function (w/ Regularization) ... \n')

lambd = 1 # with regularization of lambda = 1

cost = getCost(np.copy(nn_params), input_layer_size, hidden_layer_size, num_labels, X_org, y_org, lambd)

# After regularization cost
print('Cost at parameters (loaded from ex4weights):', cost, '\n(this value should be about 0.383770)\n')

# Part 5 Evaluating Sigmoid Gradient

tmpArray = np.array([-1, -0.5, 0, 0.5, 1])
sigmGResults = sigmoidGradient(tmpArray)

print('Sigmoid Gradient Results', sigmGResults)

# Part 6 Random Initialization
initial_Theta1 = rand(input_layer_size, hidden_layer_size)
initial_Theta2 = rand(hidden_layer_size, num_labels)

