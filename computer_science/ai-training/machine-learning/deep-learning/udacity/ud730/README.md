# Deep Learning by Google

[Course link](https://in.udacity.com/course/deep-learning--ud730)

## Quizes

1. [Softmax](https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/63815621490923) - [Code](softmax.py)
2. [Numerical Stability](https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/71235296110923) - [Code](numerical_stability.py)

## Notes
* Softmax function which converts classified labels scores into probabilities. Softmax Function S(yi) = exp(yi) / Sigsum(exp(yi))
* One-hot Encoding: Needed a way to represent the labels mathematically. The probabilities of correct class is close to 1.0 and all the other classes are close to 0.0, so the vector representation of same thing is called one-hot encoding.
* Cross Entropy: Natural way of comparing two probability vectors is called Cross Entropy. D(S,L) = - sigsum(Li*log(Si)). D = Distance, S = Distributions of softmax, L = Labels which are one-hot encoded.
* Multinomial Logistic Classification D(S(WX+b), L)
* Minimizing Cross Entropy: Calculate the average cross entropy or training loss l = (sigsum,i(D(S(wxi + b), Li)))/N. For example Imagine loss (l) is function w1 and w2 which will be small in some areas and small in othe, our objective is to find the loss minimum for the given weights, we can use "Gradient Descent" and take the derivate - (alpha)(delta(l(w1, w2))) follow that derivative by taking step backwards, and repeat until you get to the bottom. 
* The average cross entropy or training loss should never be too big or too small. In either cases it leads to errors. Check the [numerical stability](numerical_stability.py). So the guiding principles that we always have mu(Xi) = 0 i.e zero Mean, variance(Xi) = variance(Xj) i.e equal variance whenever possible.
* Initial Values: Draw the weights randomly from a Gaussian distribution with mean zero and standard deviation sigma.The sigma value determines the order of magnitude of your outputs at the initial point of your optimization. Because of the soft max on top of it, the order of magnitude also determines the peakiness of your initial probability distribution. A large sigma means that your distribution will have large peaks.It's going to be very opinionated. A small sigma means that your distribution is very uncertain about things. It's usually better to begin with an uncertain distribution and let the optimization become more confident as the train progress. So use a small sigma to begin with.
* Training completion / stop state: optimization package computes the derivative of this loss with respect to the weights and to the biases and takes a step back in the direction opposite to that derivative. And then we start all over again, and repeat the process until we reach a minimum of the loss function. w <- w -(alpha)(delta,w(loss fn)), b <- b - (alpha)(delta,b(loss fn)). delta,w is partial derivative with respect to 'w'
