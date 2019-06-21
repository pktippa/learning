function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta



X_x_theta = X * theta;
h_theta = sigmoid(X_x_theta);
log_h = log(h_theta);
log_1_h = log( 1 - h_theta );

J = (-1/m) * (log_h' * y + log_1_h' * (1-y)) + (lambda / (2 * m)) * (theta' * theta - theta(1) ** 2) ;
funny_mat = eye(length(theta));
funny_mat(1,1) = 0;
grad = (1 / m) * ( X' * (h_theta - y) + lambda * (funny_mat * theta));


% =============================================================

end
