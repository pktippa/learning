# Steps
# 1. Import Dataset
# 2. Train a classifier
# 3. Predict label for a new flower
# 4. Visualize the tree.
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
# https://en.wikipedia.org/wiki/Iris_flower_data_set
iris = load_iris()
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# print(iris.feature_names)
# ['setosa' 'versicolor' 'virginica']
# print(iris.target_names)
# [ 5.1  3.5  1.4  0.2]
# print(iris.data[0])
# 0
# print(iris.target[0])
# The three different types of flowers are distributed equally 50 per each
# 0-49 -> setosa, 50-99 -> versicolor, 100-149 -> virginica
# Indexes of each flower type as part of test data
test_idx = [0, 50, 100]

# training data, removing the test data from the original data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# Creating the classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# Our test target is [0 1 2] which we removed from the original target data
# to form training data
print(test_target)

# Now lets see what the prediction results, see it also results [0 1 2]
# So the classifier predicts exactly.
print(clf.predict(test_data))

# Now visualizing data, got the code from 
# http://scikit-learn.org/stable/modules/tree.html#classification
import pydotplus
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("iris.pdf")
