import numpy as np

from regresspy.loss import mae, sse, mse, rmse


def test_mae():
    dummy_predictions = np.array([2.0, 4.0, 7.0, 8.0])
    dummy_labels = np.array([1.0, 3.0, 6.0, 7.0])
    dummy_mae = 1.0
    assert mae(dummy_predictions, dummy_labels) == dummy_mae


def test_sse():
    pass


def test_mse():
    pass


def test_rmse():
    pass
