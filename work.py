import numpy as np
import scipy as sp


# Task 1:
def percent_of_mean(stock_idx):
    """
    Calculate the percentage of each stock index relative to the mean of indices.

    :param stock_idx: A 1-D array containing the values for daily stock indices.
    :type stock_idx: numpy.ndarray

    :return percent_vals: A list of floats representing the percent value of each stock index relative to the mean of
    indices.
    :rtype: list[float]

    """
    # Get the mean of the stock indices.
    mean = np.mean(stock_idx)

    # Calculate the percentage value for each stock index relative to the mean
    percent_vals = (stock_idx / mean) * 100

    return percent_vals


