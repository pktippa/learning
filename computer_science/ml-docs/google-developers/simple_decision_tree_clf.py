# Simple Decision tree classifier
from sklearn import tree
# features are input to classifier and labels are the output
# Since scikit-learn uses real valued features, represent features in numerical values.
# 0 for bumpy, 1 for smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# 0 for apple, 1 for orange
labels = [0, 0, 1, 1]
# Creating a classifer object
clf = tree.DecisionTreeClassifier()
# Giving the training data to classifier to get trained
clf.fit(features, labels);
# The prediction should be 1, since that is what we gave in our training data.
print(clf.predict([[150, 0]]))
