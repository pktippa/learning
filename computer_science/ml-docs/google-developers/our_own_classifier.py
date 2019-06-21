# Classifier is a scrappy version of K nearest neighbors.
# Taking the code from basic_pipeline.py and implement our own version

from scipy.spatial import distance

# Eucledian distance or Straight line distance between two points
# sqrt(a**2 + b**2)
def euc(a, b):
    return distance.euclidean(a, b)

# Our own scrappy K nearest neighbors classifier
class MyOwnKNN:
    # Implementing fit method for in interface
    # Memorizes the training data.
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # Implementing predict method for interface
    # Returns predictions in an array
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    # Returns the closest point in the training set
    # as K nearest neighbor predicts the near one as the value.
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

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

my_classifier = MyOwnKNN()

# Training the data with classifier
my_classifier.fit(X_train, y_train)

# Getting the predictions.
predictions = my_classifier.predict(X_test)

# We can check how accuracy our classifier is with an utility
from sklearn.metrics import accuracy_score
# Accuracy test with actual to predicted values
print(accuracy_score(y_test, predictions))