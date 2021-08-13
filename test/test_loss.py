import numpy as np

from regresspy.loss import mae, sse, mse, rmse


def test_mae():
    dummy_predictions = np.array([2.0, 4.0, 7.0, 8.0])
    dummy_labels = np.array([1.0, 3.0, 6.0, 7.0])
    dummy_mae = 1.0
    assert mae(dummy_predictions, dummy_labels) == dummy_mae


def test_sse():
    dummy_predictions = np.array([5.0, 4.0, 7.0, 8.0])
    dummy_labels = np.array([2.0, 3.0, 8.0, 9.0])
    dummy_sse = 1.0
    assert sse(dummy_predictions, dummy_labels) == dummy_sse


def test_mse():
    dummy_predictions = np.array([3.0, 7.0, 7.0, 9.0])
    dummy_labels = np.array([9.0, 8.0, 1.0, 2.0])
    dummy_mse = 1.0
    assert mse(dummy_predictions, dummy_labels) == dummy_mse


def test_rmse():
    dummy_predictions = np.array([3.0, 7.0, 7.0, 9.0])
    dummy_labels = np.array([6.0, 2.0, 1.0, 2.0])
    dummy_rmse = 1.0
    assert rmse(dummy_predictions, dummy_labels) == dummy_rmse
