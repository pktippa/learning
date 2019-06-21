# If you are doing a binary classification it is easy to decide between two different things.
# Lets take an example to trying to classify type of dog between Greyhound and labrador
# Here we will take two features dog height in inches and eye color.
# Firt we will say the Greyhounds are usually taller than the Labradors, next we will pretend
# there are only two eye colors blue and brown and we say the color of the dog doesnt depend
# on the color of the dog. This leads to one of the feature is useful and other gives nothing.

# Height in inches
# Well on an average the Greyhounds are couple of inches taller than the Labrador, but not always
# there is lot of variation in this world. So when we think about the feature we have to consider
# how it looks for different values in a population.

# Going to code 
import numpy as np
import matplotlib.pyplot as plt

# Taking an example of 1000 dogs, split equally for greyhounds and labradors
greyhounds = 500
labs = 500

# Taking general greyhound height 28 inch and lab height 24 inch and plus random
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

# Plotting a histogram giving red color to greyhounds and blue color to labs
plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()

# If you see and analyze the histogram, starting from left at 20 inches,
# if you are asked to predict, the most probability it is a lab, since most of them are in blue.
# then starting from right 30 or 35 inches, the most probability it is a greyhound
# but the data in the middle, has equal distribution not able to make the proper prediction since
# the probabitily of each dog is close and same.

# So the feature Height is useful but it is not perfect.

# So that's why in Machine learning we take multiple features into account for learning and predictions.

# Do a thought experiment as if you are a classifier and what features you need to classify, for our example
# like their hair length, how fast they run, how much they weight

# Now lets take the eye color
# Since the eye color doesnt depend on the type of dog, there is equal probability of
# greyhound and lab, so there is 50-50 and the featyue doesnt correlate what type of dog.

# Including this clueless feature like this (eye color) into the training data hurt
# your classifier accuracy thats because they might appear useful purely by accident
# especially when you have small amount of training data.

# Always use the features that are independent, since they give you different type of information
# Imagine we already have a feature 'height in inches' what if we take feature 'height in centimeters'
# it will not be helpful since it is already corelated, so always remove the highly corelated features
# from your training data, or avoid redudant features, since not all classifiers are intelligent
# to know the there is a corelation between the features so they double count how important
# this feature is.

# Features should be easy to understand. lets take the example of how many days it would take between
# two cities, it is always good to have no.of miles as feature rather than having the GPS coordinates
# of the cities which is a complex why because we can have a look at no.of miles and make a good guess
# but learning the relation between LAT, LON and time is much harder and would require many more examples
# in your training data

# Ideal Features are
# 1. Informative
# 2. Independent
# 3. Simple
