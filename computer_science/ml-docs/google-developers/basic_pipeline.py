# A classifer is a function f(x) = y, where f(x) is features and y is label/target

# importing a dataset
from sklearn import datasets
iris = datasets.load_iris()

# taking features
X = iris.data
# taking lables
y = iris.target

from sklearn.cross_validation import train_test_split
# Partitioning into train and test data equally(test_size = .5)
# X_train, y_train are for training and X_test, y_test are for testing.
# the train and test split will be random, so the accuracy may be different 
# when you ran multiple times.
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = .5)

# Now lets see how different classifiers perform the prediction of same.

# Decsion tree Classifier
# from sklearn import tree
# Initializing Decision Tree classifier
#my_classifier = tree.DecisionTreeClassifier()

# K Neighbors Classifier
from sklearn.neighbors import KNeighborsClassifier
# Initializing KNeighborsClassifier
my_classifier = KNeighborsClassifier()

# There are different classifiers but under the hood the methods are same,
# so even we use Decision Tree or K Neighbor classifiers or any other
# the interface methods .fit and .predict are same.

# Training the data with classifier
my_classifier.fit(X_train, y_train)

# Getting the predictions.
predictions = my_classifier.predict(X_test)

# We can check how accuracy our classifier is with an utility
from sklearn.metrics import accuracy_score
# Accuracy test with actual to predicted values
print(accuracy_score(y_test, predictions))

# Now lets see what is meant by learn from data, recollect f(x) = y,
# here the feautres are x and labels are y, and these are input and output of 
# a function.
# Now we already know a function from the programming
"""
def classify(feautures):
    # do some logic
    return label
"""
# In supervised learning we dont want to write this classify function by ourselves
# we want an algorithm to learn from the training data, so lets see what is meant by
# learn a function. We know a function is mapping of input to output values, lets take
""" y = mx + b """ 
# Simple line function, so for the classifier the input X is features and out y is the label
# from our classify function above like spam or not spam, type of flower, so what could the body
# of the function look like, thats the part what we want to write algorithmically or learn.
# We are not starting from scratch for the body of the function out of thin air, instead we
# start with a model. A model is the prototype for or the rules for defining the body of our
# function. Typically a model has parameters that we can adjust with our training data.
# Lets see high level how this process works, wanted to classify group of red dots on right side and
# group of green dots on left side of XY two dimensional plane, the line function y = mx + b can be classifier
# for example, lets see how will be learn this line, one way is to use the training data to adjust
# the parameters of the model - the line function, so we have only two parameters to adjust the line
# m and b and changing them we can change the line appears, so how can we learn the right parameters
# one way is that we can iteratively adjust them using our training data for example we might start with a random 
# line with m and b and use to classify the first training example if it gets it right we dont have to change the line
# so we move on to next example but on the other hand if it gets wrong we can slightly adjust the parameters of our model
# to make it more accurate. One way to think of learning using training data to adjust the parameters of a model.
# Have a look at http://playground.tensorflow.org
