# Coursera Machine Learning - Standford

In Separate Project: Find [here](https://github.com/pktippa/datasciencecoursera)

* Linear Regression with One Variable or Univariate linear Regression.
* Hypothesis (h) is for mapping x's to y's 

To approach a problem for Linear regression, take few values of theta and try to plot same on the data points with line and see how the line cuts through the data.

Idea: Choose theta0, theta1 so that h(x) is close to y for our training example (x, y).

h_theta(x) = theta0 + theta1 * x

Cost Function or Squared Error Function or Mean Squared Error

J(theta0, theta1) = 1/2m(Sigma[i - 1 to m](h_theta(x)(i) - y(i)))^2

Optimization objective is to minimize the Cost Function

Try putting the constants in equation to zero in h_theta(x) = theta0 + theta1 * x

Lets say theta0 = 0, for various values of theta1, try to plot h_theta(x) and J(theta)

J(theta) will be a U shaped Parabola, having lowest point when theta1 = 1.
Why?

since theta0 = 0, h_theta(x) = theta1 * x;
if theta1 = 1 -> h_theta(x) = x

to have minimum value of Cost Function J -> 0 -> we need h_theta(x) = y, so the difference between them would be zero.

Contour Plots:

Converting the 3D plot to 2D plot by showing in ellipses.

Gradient Descent:

alpha - learning rate.

Simultaneous updates

temp0 := theta0 - d(J(theta0, theta1))/d(theta0)
temp1 := theta1 - d(J(theta0, theta1))/d(theta1)

theta0 := temp0
theta1 := temp1

The way we do this is by taking the derivative (the tangential line to a function) of our cost function. The slope of the tangent is the derivative at that point and it will give us a direction to move towards.

https://www.cliffsnotes.com/study-guides/calculus/calculus/applications-of-the-derivative/tangent-and-normal-lines

Negative slope and positive slope of a line can be found by looking at the line direction, like as x increases, does y increase or not.

The cost function for linear regression is always a bowl shaped or convex shaped function.

So it always has a global optimum but not a local optimum.

Using all the training examples to calculate new values of parameters(Ex: theta0, theta1) is called Batch Gradient Descent.

A vector is a special matrix with only one column!

For showing in form of matrices, the hypothesis parameters are formed in vector.i.e
[ theta0 ]
[ theta1 ]

it is a 2 dimensional vector .ie. 2 x 1 matrix

Matrix dont have a inverse is called "singular" or "degenerative"

A non square matrix does not have an inverse matrix

In matrix notations, the parameters are in n-dimensional vector.

so hypothesis becomes

h_theta(x) = theta(Transpose) * X

where

X =

X0
X1
X2

theta = 

theta0
theta1
theta2

n+1 dimensional vectors

and
theta(Transpose) = [theta0 theta1 theta2] ; row vector

h_theta(x) will get a real number.

remember X1, X2, X3 are always feature vectors

TODO - need visually
Actually the original data table if you visualize it will be transposed for all features

x(i)j = value of feature j in the ith training example
x(i) =the input (features) of the ith training example
m=the number of training examples
n=the number of features

Linear regression with multiple variables is also known as "multivariate linear regression".

See imgs\linear_regression_with_multiple_variables.PNG

Some times the multivariate linear regression may not work with look at the data
So choose the polynomial regression with features as x^2, x^3,sqrt(x).
Make sure you do the feature scaling.

there are algorithms to get to know which features to use for building the algorithm.

## Automatically finding the parameters - theta

We can use normal equation method, as the Cost function J is a quadratic function of theta(if there is only one parameter).

So to minimize any function we need to take derivative of the function and make it equal to zero. i.e d(J(theta))/dtheta = 0

Similarly for multiple theta parameters theta0, theta1, theta2 - take corresponding partial derivate and make it equal to 0

Normal Equation method 

theta = (X`X)^-1 * (X`)* y, where X` is X transpose

The cost of calculating inverse for n dimensions is O(n^3)

Normal equation method does not fit for Classification problems, it is more suitable for linear equation with number of features >= 10,000

Classification to 0 or 1:
0 - Negative class - specifying non presence of something - Not Spam - Benign
1 - Positive Class - Specifying presence of something - Spam - Malignant

Trying to apply a linear regression to classification problem isnt a good idea.
Lets say first the hypothesis going through middle of points, with some angle from x axis
Resulting in lets say if the value is >=0.5 it is Positive (1), or <0.5 it is Negative (0)
Now if we add another point to the right far from the current dataset, the line moves in the direction
reducing the angle towards the X axis, resulting in the threshold value meeting the line in 
towards the right direction, making some of the positive examples marking as negative.

h_theta(x) = estimated probability that y=1 on input x

Ex: h_theta(x) = 0.7, i.e 70% probability that the tumor is a malignant

h_theta(x) = P(y=1 | x;theta) Probability for y=1 given x and parameterized theta

Decision boundary

it the curve/line which separately the positive and negative classes
i.e for y =0 , y =1 when we plot the graph for features
with identified theta values.

i.e. h_theta(x) = g(theta_trans * X ) 

here theta_trans * X = 0 is the line or curve which separates the positive and negative classes

this is the property of hypothesis even with the training samples plotted on graph.

Ex: -3 * x1 + 2 * x2 = 0 is a line


Understand Maximum likelyhood of estimation.

For multi class classification problem we use one-vs-all classification

one-vs-all : For mutiple calsses lets say triangles, sqaures, crosses. We divide this into 3 binary
classification problems
1. take triangles as positive class, then convert squares, crosses into circles which is a negative class
calculate h_theta_1(x)
2. take squares as positive class, then convert trianges, crosses into circles which is a negative class
calcuate h_theta_2(x)
3. take crosses as positive class, then convert triangles, squares into circles which is a negative classs
calculate h_theta_3(x)

For prediction, take max of h_theta_1, h_theta_2, h_theta_3

For Fixing overfitting we use regularization

Underfitting also called High Bias.

Overfit also called "high Variance"

Regularization:

We will penalize heavily for the theta parameters for the the features are making overfitting of data.

Lets say a higher order polynomial function is chosen to fit the data as hypothesis

h_theta(x) = theta_0 + theta_1 * x + theta_2 * x^2 + theta_3 * x^3 + theta_4 * x^4

For cost J

J(theta) = (1/2m) Sigsum[ (h_theta(x) - y )^2 ]

modify to penalizing the theta_3 and theta_4

J(theta) = (1/2m) Sigsum[ (h_theta(x) - y )^2 + theta_3^2 * 1000 + theta_4^2 * 1000 ]

Resulting which the theta_3 and theta_4 should be very very small i.e. near to 0

resulting in the hypothesis function has less effect with theta_3 and theta_4, so h(x) becomes

h_theta(x) = theta_0 + theta_1 * x + theta_2 * x^2

For regularizing all the parameters of theta (Observe m and n)

min_theta (1/2m) Sigsum_1_to_m [ (h_theta(x) - y)^2 ] + lambda * Sigsum_1_to_n [ theta_j ^2 ]

last term is regularization term and lambda is regularization parameter.


Neural Networks:

If network has s(j) units in layer j and s(j+1) units in layer j+1, then Θ(j) will be of dimension
s(j+1) × ( s(j) + 1 ) 

Lets say s(j) is x1, x2, x3 and s(j+1) is a1, a2, a3, a4
For which the bias term x0 adds to s(j) that is the plus one.

For theta(trans) * s(j) = s(j+1) -> theta should have rows as number of s(j+1) and columns
as (s(j) + 1), here +1 is for bias term.

Cost function for neural networks

J is a real value or scalar BUT NOT a vector
let K be number of output classes
m is anyway training examples
L be number of layers

J = - (1/m) ( sigsum_m( sigsum_K( yk * log(hk) + (1-y) * (1 - log(hk))) )) 
            + (lambda/2m) ( sigsum_L( sigsum_K( sigsum_m(theta_^2) ) ) )



Symmetry breaking:

If we initialize theta values with 0, it would get into symmetry.