import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

import stocks


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


# Task 2:
plt.plot(stocks.trading_days, percent_of_mean(stocks.djia), label="DJIA", color='blue')
plt.plot(stocks.trading_days, percent_of_mean(stocks.sp500), label="S&P500", color='green')
plt.plot(stocks.trading_days, percent_of_mean(stocks.nasdaq), label="NASDAQ", color='red')
plt.xlabel("Trading Days since Jun 1, 2016")
plt.ylabel("Percent of Mean")
plt.xlim(left=0, right=70)
plt.ylim(bottom=90, top=106)
plt.tick_params(direction='in', axis='both', which='both')
plt.legend(loc='best')
plt.savefig('HW2 Task 2 Plot')
plt.close()

#Task 3:
def num_days_big_percent_chg(stock_idx, percent):
    """
    Calculate the number of trading days when the magnitude of percent change since the previous day is greater than
    the given percent.

    :param stock_idx: A 1-D array containing the values for stock indices. :type stock_idx: numpy.ndarray :param
    percent: A number that represents the threshold percentage change. :type percent: float :return num_days: The
    total number of trading days when the magnitude of percent change exceeded the given percentage. :rtype: int

    """
    percent_changes = np.abs((stock_idx[1:] - stock_idx[:-1] / stock_idx[:-1]) * 100)
    exceeds_threshold = percent_changes > percent
    num_days = np.sum(exceeds_threshold)
    return num_days

