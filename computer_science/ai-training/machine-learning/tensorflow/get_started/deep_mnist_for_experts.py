# Coded from https://www.tensorflow.org/get_started/mnist/pros
# Download, extract and read the data Automatically
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# Importing tensorflow
import tensorflow as tf

# Create the model
x = tf.placeholder(tf.float32, [None, 784])

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])

# Function to initialize weight variable with given shape
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

# Function to initialize bias variable with given shape
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# Helpful function to do convolution
# Our convolutions uses a stride of one and are zero padded so that the output is the same size as the input
def conv2d(x, W):
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# Helpful function to do max pooling
# Our pooling is plain old max pooling over 2x2 blocks.
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# First Convolution Layer
# The convolution will compute 32 features for each 5x5 patch
# The passed shape [5, 5, 1, 32] for weight variable, the first two dimensions are the patch size, the next is the number of input channels, 
# and the last is the number of output channels. We will also have a bias vector with a component for each output channel.
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# To apply the layer, we first reshape x to a 4d tensor, with the second and third dimensions 
# corresponding to image width and height, and the final dimension corresponding to the number of color channels.
x_image = tf.reshape(x, [-1, 28, 28, 1])

# We then convolve x_image with the weight tensor, add the bias, apply the ReLU function, 
# and finally max pool. The max_pool_2x2 method will reduce the image size to 14x14.
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# Second Convolution Layer
# In order to build a deep network, we stack several layers of this type. The second layer will have 64 features for each 5x5 patch.
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# Densely or Fully Connected Layer.
# Now that the image size has been reduced to 7x7, we add a fully-connected layer with 
# 1024 neurons to allow processing on the entire image. We reshape the tensor from the pooling layer 
# into a batch of vectors, multiply by a weight matrix, add a bias, and apply a ReLU.

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Dropout
# To reduce overfitting, we will apply dropout before the readout layer. 
# We create a placeholder for the probability that a neuron's output is kept during dropout. 
# This allows us to turn dropout on during training, and turn it off during testing. 
# TensorFlow's tf.nn.dropout op automatically handles scaling neuron outputs in addition to masking them, 
# so dropout just works without any additional scaling.

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# Final or Readout Layer
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# Same as previous Softmax regression model
# using AdamOptimizer rather than GradientDescentOptimizer
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Running with in Session
with tf.Session() as sess:
    # Initializing all variables
    sess.run(tf.global_variables_initializer())
    # Running for 20000 iterations
    for i in range(20000):
        batch = mnist.train.next_batch(50)
        # Checking the training accuracy for every 100th step
        if i % 100 == 0:
            # Since we should not do any dropout passing the value of keep_prob as 1.0
            train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
            print('step %d, training accuracy %g' % (i, train_accuracy))
        # Running training on the given batch with dropout 0.5
        train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
    # Printing the Final test accuracy.
    print('test accuracy %g' % accuracy.eval(feed_dict={
      x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))