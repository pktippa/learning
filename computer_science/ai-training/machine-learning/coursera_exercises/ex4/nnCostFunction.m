function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

B_delta_1_sum_term = Theta1_grad;
B_delta_2_sum_term = Theta2_grad;

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% First layer
a1 = [ones(m, 1) X];
z1 = a1 * Theta1';
h1 = sigmoid(z1);

% Second Layer
a2 = [ones(m, 1) h1];
z2 = a2 * Theta2';
h2 = sigmoid(z2);

log_h = log(h2);
log_1_h = log( 1 - h2 );

term = zeros(num_labels, 1);

%fprintf('y _ 1');
%y(1)

%fprintf('h_theta _ 1');
%h2(1, :)
for iter = 1:m
    % Copying all zeros vector
    temp = term;
    % setting the corresponding class value to 1, and rest all being 0
    temp(y(iter)) = 1;
    % Summing up the cost 
    % h is of shape 5000, 10 -> 5000 rows with 10 columns,
    % here 10 columns corresponding to 10 classes
    % so h(i, :) is a row vector for Ex: value 10 -> [0.01  0.01  .... 0.99]
    % this we need to multiply with y column vector -> [0 0 0 ... 1]
    J += (-1/m) * (log_h(iter, :) * temp + log_1_h(iter, :) * (1-temp));
    %if iter < 10
    %    J
    %end
end

% regularization cost 
% we dont have to regularize the first term theta 0

temp1 = Theta1;
temp1(:, 1) = 0;

temp2 = Theta2;
temp2(:, 1) = 0;

J += (lambda / ( 2 * m ) ) * (sum( sum( temp1 .* temp1 ) ) + sum ( sum( temp2 .* temp2 ) ));
classes = [1:num_labels];
for i = 1:m
    % Getting ith training example
    x1 = X(i, :); % (1, 400)
    %fprintf('%f', size(x1));
    % Getting first activation example
    a1 = [1 x1]; % (1, 401)
    z1 = a1 * Theta1'; % (1, 25)
    h1 = sigmoid(z1); % (1, 25)
    
    % For third layer
    a2 = [1 h1]; % (1, 26)
    z2 = a2 * Theta2'; % (1, 10)
    h2 = sigmoid(z2); % (1, 10)

    %fprintf('\n y(i) %f', size(y(i)));
    %fprintf('\n h2 %f', size(h2));
    %(classes == y(i))
    s_delta_3 = h2 - ( classes == y(i) ); % (1, 10)
    %fprintf('\n%f', size(s_delta_3));
    s_delta_2 = ( s_delta_3 * Theta2 ) .* sigmoidGradient( [1 z1] ); % (1, 26)

    % Removing the first element in vector that is s_delta_0_2
    s_delta_2 = s_delta_2(2:end); % (1, 25)

    B_delta_2_sum_term += s_delta_3' * a2;  % (10, 1) X (1, 26) = (10, 26)
    B_delta_1_sum_term += s_delta_2' * a1;  % (25, 1) X (1, 401) = (25, 401)

end

Theta2_grad = (1/m) * B_delta_2_sum_term;
Theta1_grad = (1/m) * B_delta_1_sum_term;

% For Adding regularization term
Theta1(:, 1) = 0;
Theta2(:, 1) = 0;

Theta1_grad += (lambda / m) * Theta1;
Theta2_grad += (lambda / m) * Theta2;
% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

%fprintf('Size %f', size(J));
end
