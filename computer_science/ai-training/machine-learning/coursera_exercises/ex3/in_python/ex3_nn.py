import numpy as np

from exercises.sigmoid import sigm

# First layer Theta values
Theta1 = np.genfromtxt('../Theta1.csv', delimiter=',')
print('Theta1 shape, ', Theta1.shape)
# We wanted to have the transpose value
Theta1 = Theta1.T

# Second Layer theta values

Theta2 = np.genfromtxt('../Theta2.csv', delimiter=',')
print('theta 2 shape', Theta2.shape)
# We wanted to have the transpose value
Theta2 = Theta2.T

num_labels = Theta2.shape[1]

X_org = np.genfromtxt('../X_input.csv', delimiter=',')
y_org = np.genfromtxt('../y_output.csv', delimiter=',')

y_org = y_org.reshape((len(y_org), 1))

print('X shape', X_org.shape)
print('y shape', y_org.shape)

# First layer input
a1 = np.concatenate((np.ones((X_org.shape[0], 1)), X_org), axis=1)
z1 = a1.dot(Theta1)

# First layer output
h1 = sigm(z1)

print('h1 shape', h1.shape)
# Second Layer input
a2 = np.concatenate((np.ones((h1.shape[0], 1)), h1), axis=1)
z2 = a2.dot(Theta2)

# Second layer output
h2 = sigm(z2)

print('shape of h2', h2.shape)

pred = np.argmax(h2, axis=1)
pred = pred.reshape((len(pred), 1))
pred = pred + 1 # Since index starts at 0

comparison = (pred == y_org)

accuracy_ = np.zeros((len(y_org), 1))
accuracy_[comparison] = 1

print('Accuracy of neural network', np.mean(accuracy_))