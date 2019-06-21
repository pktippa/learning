"""Softmax.
For a given scores as n-dimensional array of where each column represents a sample
the softmax should return the probabilities of same n-dimensional array with same shape.
The probabilities for each sample (column) must sum to 1

Softmax Function S(yi) = exp(yi) / Sigsum(exp(yi))
"""

scores = [3.0, 1.0, 0.2]
import numpy as np
import math

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # The longest way, some bug in code even though the approach is same to calculate softmax
    """
    probabilities_array = list()
    x_contains_array_el = False
    x_denom = 0
    for ele in x:
        if isinstance(ele, np.ndarray):
            x_contains_array_el = True
            tmp_probabilities_array = list()
            tmp_el_denom = 0
            for el in ele:
                tmp_el_denom += math.exp(el)
            for el in ele:
                tmp_prb = math.exp(el) / tmp_el_denom
                tmp_probabilities_array.append(tmp_prb)
            probabilities_array.append(tmp_probabilities_array)
        # Assuming either it is just a single value list or its a pure numpy array with defined shape.
        else:
            #x_denom += math.exp(ele)
            x_denom += ele
    if not x_contains_array_el:
        for ele in x:
            probability = math.exp(ele) / x_denom
            probabilities_array.append(probability)
    return np.array(probabilities_array)
    """
    # The shortest way and the efficient way as per tutorial.
    return np.exp(x) / np.sum(np.exp(x), axis=0)

print(softmax(scores))
#scores = np.array([3.0, 1.0, 0.2])

# Multiply Scores with 10
# If we multiply the scores by 10, the probabilites go close to 1.0 or 0.0
#print(softmax(scores * 10))

# Divide Scores with 10
# If we divide the scores by 10, the probabilities go to uniform distribution, 
# reaching to value of 1/len(array). Ex: for scores with 3 elements, it gets close to 1/3 => 0.333 
#print(softmax(scores / 10))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
