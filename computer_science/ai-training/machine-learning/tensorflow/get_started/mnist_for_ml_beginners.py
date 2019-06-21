# Download, extract and read the data Automatically
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# The program uses softmax regression, read more about softmax 
# http://neuralnetworksanddeeplearning.com/chap3.html#softmax

# Printing the shape of dataset, it returns 
# Images X (55000, 784)
# Labels Y (55000, 10)
print('Train images shape ', mnist.train.images.shape)
print('Train labels shape ', mnist.train.labels.shape)

# Predicting using softmax regression uses below format in matrix representation
# Y = softmax(XW + b)

# Importing tensorflow
import tensorflow as tf

# Creating placeholder for variable X
# None means that a dimension can be of any length
# 784 because the 2nd dimension of train set is also 784
X = tf.placeholder(tf.float32, shape=(None, 784))

# Initializing Weights W variable with shape as (784, 10)
# Since we are going to Matrix Multiply X to W and want to have returned
# matrix in labels Y shape(, 10).
W = tf.Variable(tf.zeros(shape=(784, 10)))

# Bias is added so that we want to be able to say that some things are more likely independent of input
# Initializing Bias b variable with shape as (10)
# So that matrix addition would be possible
b = tf.Variable(tf.zeros(shape=(10)))

# Now lets build predictions
# we can also use tf.add() apart from the + operation
# Matrix Multiplying X and W, adding bias and then applying softmax on result
y = tf.nn.softmax(tf.matmul(X, W) + b)

# Using Cross-Entropy as the cost function, you can read more about it in ml-basics repo
# Creating new placeholder to input correct answers to build cross entropy error
y_ = tf.placeholder(tf.float32, shape=(None, 10))

# Calculating cross-entropy
# Hy'(y) = - sigsum(i, y'i * log(yi))
# Where y is predicted probability distribution, y' is the true distribution
# Then tf.reduce_sum adds the elements in the second dimension of y, due to the reduction_indices=[1] parameter
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# we don't use this cross_entropy formulation, because it is numerically unstable. 
# Instead, we apply tf.nn.softmax_cross_entropy_with_logits on the unnormalized logits
# Where labels are actual labels, logits are the predicted values.
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

# We are asking tensorflow to minimize cross_entroy using gradient descent with a learning rate of 0.5. 
# Gradient Descent shifts each variable a little bit in the direction that reduces the cost.
# tensorflow automatically does the backpropagation algorithm to efficiently determine how your variables
# affect the loss you ask to minimize.
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# All tensorflow computational graphs run on session.
# Normally we create a graph and then run the graph on a session, for this program we create interactive session
sess = tf.InteractiveSession()

# Initializing all variables
tf.global_variables_initializer().run()

# Now running the training step 1000 times
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={X: batch_xs, y_: batch_ys})

# tf.argmax is an extremely useful function which gives you the index of the highest entry in a tensor along some axis
# Ex: sess.run(tf.arg_max([1,2,35,4], 0)) returns 2, which is the index of value 35
# tf.equal to check if our prediction matches the truth.
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# Casting predictions to floating points [True, False, True, True] would become [1,0,1,1]
# then take mean which will give the accuracy.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Getting the accuracy of our model, by feeding test images and labels.
print('Testing accuracy : ', sess.run(accuracy, feed_dict={X: mnist.test.images, y_: mnist.test.labels}))