# Math Functions

## Hypothesis Function - h

## Cost Function - J

To Measure the accuracy of Hypothesis function (h) we use Cost function (J).

For Linear Regression

J(theta) = (1/2m) Sigsum_1_to_m (h_theta(x) - y) ^ 2

For Logistic Regression

Cost(h_theta(x), y) = -log(h_theta(x)) if y = 1
                    = -log(1 - h_theta(x)) if y = 0

For always y being 1 or 0. we can rewrite the above function into one

Cost(h_theta(x), y) = -y * log(h_theta(x)) - (1-y) * log(1 - h_theta(x))

## Logistic function or Sigmoid Function - g(z)

g(z) = 1 / (1 + e^-z)

## Non Convex function

it can have more local minima / optimum