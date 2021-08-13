from numpy.lib.npyio import load
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression    
from regresspy.regression import Regression
from regresspy.loss import rmse


iris = load_iris()
# We will use sepal length to predict sepal width
X = iris.data[:, 0].reshape(-1, 1)
Y = iris.data[:, 1].reshape(-1, 1)

#TODO Perform a linear regression using sklearn and calculate training rmse.

#Linear regression initialized above successfully                                                                                        

model = LinearRegression()
model.fit(X,Y)
final_predictions = model.predict(X)
final_mse = mean_squared_error(Y, final_predictions)
final_rmse = np.sqrt(final_mse)

# Use the SGDRegressor and only select set learning rate and epochs.
sgd = SGDClassifier(
    loss='log',
    penalty='none',
    max_iter=1000,
    early_stopping=True,
    n_iter_no_change=10,
    tol= 0.001,
    validation_fraction=0.1,
    learning_rate=0.0001,
    eta0=0.1,
    verbose=1
)
sgd.fit(X, Y)

#TODO Perform a linear regression using your code and calculate training rmse.
model = Regression()
model.fit(X,Y)
predicted_values = model.predict(X)
training_rmse = rmse(Y,predicted_values)
