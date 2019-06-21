# Convolutional Neural Networks

Giving the Neural Network to understand the translation invariance.

Convolutional Neural Networks or CovNets are neural networks that share their parameters across space.

Patches are also called Kernels.

Stride: It is the no of pixels that you're shifting each time you move your filter.

A stride of 1 makes the output roughly the same size as the input, a stride of 2 means it's half the size.

When you don't go past the edge of image it is called "Valid Padding".

When you go off the edge and pad with zeros in such a way that the output map size is exactly the same as the input map, this is called "Same Padding".


The more convolution steps you have, the more complicated features your network will be able to learn to recognize. For example, the first convolution step might learn to recognize sharp edges, the second convolution step might recognize beaks using it's knowledge of sharp edges, the third step might recognize entire birds using it's knowledge of beaks, etc.

## Constructing the Right Network

So how do you know which steps you need to combine to make your image classifier work?

Honestly, you have to answer this by doing a lot of experimentation and testing. You might have to train 100 networks before you find the optimal structure and parameters for the problem you are solving. Machine learning involves a lot of trial and error!

## Steps of Convolution from [ML is fun](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721)

1. Break the image into overlapping image tiles
2. Feed each image tile into a small neural network
3. Save the results from each tile into a new array
4. Downsampling
5. Make a prediction