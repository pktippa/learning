import math
import numpy as np

def calcSigmoid(z):
    return 1 / ( 1 + math.exp(-z) )

def sigm(X):
    sm = np.vectorize(calcSigmoid)
    return sm(X)

def sigmoidGradient(X):
    sigmV = sigm(X)
    return sigmV * ( 1 - sigmV )