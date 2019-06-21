import numpy as np
import scipy.optimize as op
from .costFunctionReg import getCost, getGrad
def optimize(X, y, theta):
    Result = op.minimize(fun = getCost, x0 = theta, args=(X, y), method='TNC', jac= getGrad, options={'maxiter': 400})
    return Result.x