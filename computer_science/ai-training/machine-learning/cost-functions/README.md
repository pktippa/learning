# Cost functions

## Cross Entropy

Hy'(y) = - sigsum(i, y'i * log(yi))

Where y is predicted probability distribution, y' is the true distribution(Ex: the one-hot encoded vector)
.More can be read [here](https://colah.github.io/posts/2015-09-Visual-Information)

## Gradient Descent

Shifts each variable a little bit in the direction that reduces the cost.

Debugging : Making sure that gradient descent is working correctly.

Plot J(theta) i.e. value of cost function with values of theta(s), vs the number or iterations.

The J(theta) value should decrease as we are going with increasing number of iterations

Try alpha learning rate with values as 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1
which are multiples of 3.

## Others

* [Logistic Regression Cost Function](log_reg_cf.md)