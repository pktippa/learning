# Decision or Classification Tree

* When a decision tree is fully grown, it is likely to overfit the training data.
* A decision tree generated from an unbalanced training data may be biased towards the majority class. In other words, it will learn the majority class, will have a high accuracy, even though, it will be unable to predict the minority class examples correctly (e.g., a dataset of 95% negative examples and 5% positive examples).
* A feature in a dataset containing all different values(which is rare), lets say if there is such a feature
  - it will be picked at the root as a first choice to split the data because it has the highest gain
  - it is the most discriminative feature 
  - it is a useless feature and should be discarded