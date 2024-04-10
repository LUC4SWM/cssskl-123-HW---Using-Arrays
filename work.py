import numpy as np
import scipy as sp


# Task 1:
def percent_of_mean(stock_idx):
    """


    :param stock_idx: A 1-D array with values for daily stock indices.
    :return: percent_vals: A list of floats representing the percent value for each stock index relative to the mean of indices.
    """
    mean = np.mean(stock_idx)
    percent_vals = (stock_idx / mean) * 100
    return percent_vals
