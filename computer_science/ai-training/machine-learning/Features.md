# Features

When there are infinite number of features Support vector machine helps you to the machine learning problems to solve it.

## Feature Scaling

See imgs/feature_scaling_01.PNG

Much skewed countours, more iterations (zig-zag) to converge
vs
Circle countor, direct path and less iterations to converge

Keep feature values with in the range of -1 to 1 , if their original range is with near
to this limits keep them as it is. ex: 0 to 3 is near to range of -1 to 1

### Mean Normalization

X1 = (X1 - Mu1) / S1

Where Mu1 = Average of all values of X1 training examples
S1 = standar deviation = max - min values of training examples 