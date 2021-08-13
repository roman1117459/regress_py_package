from numpy.lib.npyio import load
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_iris

from regresspy.regression import Regression
from regresspy.loss import rmse


iris = load_iris()
# We will use sepal length to predict sepal width
X = iris.data[:, 0].reshape(-1, 1)
Y = iris.data[:, 1].reshape(-1, 1)

#TODO Perform a linear regression using sklearn and calculate training rmse.
# Use the SGDRegressor and only select set learning rate and epochs.


#TODO Perform a linear regression using your code and calculate training rmse.

