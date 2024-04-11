"""
This file contains functions for analyzing and visualizing stock index data.

Functions:
- percent_of_mean(stock_idx): Calculate the percentage of each stock index relative to the mean of indices.
- num_days_big_percent_chg(stock_idx, percent): Calculate the number of days with a big percentage change.
- moving_average(stock_idx): Calculate the 3-day simple moving average of a stock index.
- plot_template(indices): Set up a template for plotting stock index data with a three-day moving average.

Constants:
- STOCKS_NASDAQ: NASDAQ stock index data.
- STOCKS_SP_: S&P 500 stock index data.
- DJIA: Dow Jones Industrial Average stock index data.
- DAYS: Trading days since June 1, 2016.
"""
import numpy as np
import matplotlib.pyplot as plt

# Import stocks data from the stocks module
import stocks

STOCKS_NASDAQ = stocks.nasdaq

STOCKS_SP_ = stocks.sp500

DJIA = stocks.djia

DAYS = stocks.trading_days


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


# Task 2: Plotting the percentage of each stock index relative to the mean.
plt.plot(DAYS, percent_of_mean(DJIA), label="DJIA", color='blue')
plt.plot(DAYS, percent_of_mean(STOCKS_SP_), label="S&P500", color='green')
plt.plot(DAYS, percent_of_mean(STOCKS_NASDAQ), label="NASDAQ", color='red')
plt.xlabel("Trading Days since Jun 1, 2016")
plt.ylabel("Percent of Mean")
plt.xlim(left=0, right=70)
plt.ylim(bottom=90, top=106)
plt.tick_params(direction='in', axis='both', which='both')
plt.legend(loc='best')
plt.savefig('HW2 Task 2 Plot')
plt.close()


# Task 3: Calculate the number of days with a big percentage change.
def num_days_big_percent_chg(stock_idx, percent):
    """
    Calculate the number of trading days when the magnitude of percent change since the previous day is greater than
    the given percent.

    :param stock_idx: A 1-D array containing the values for stock indices.
    :type stock_idx: numpy.ndarray
    :param percent: A number that represents the threshold percentage change.
    :type percent: float
    :return num_days: The
    total number of trading days when the magnitude of percent change exceeded the given percentage.
    :rtype: int

    """
    stock_idx = np.array(stock_idx)
    percent_changes = np.abs((stock_idx[1:] - stock_idx[:-1]) / stock_idx[:-1]) * 100
    num_days = np.sum(percent_changes > percent)
    return num_days


# Task 4: Plotting the number of days with big percentage changes for different thresholds.
pct_chg_thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]
djia_pct_chg_days = []
sp500_pct_chg_days = []
nasdaq_pct_chg_days = []
for pct in pct_chg_thresholds:
    djia_pct_chg_days.append(num_days_big_percent_chg(DJIA, pct))
    sp500_pct_chg_days.append(num_days_big_percent_chg(STOCKS_SP_, pct))
    nasdaq_pct_chg_days.append(num_days_big_percent_chg(STOCKS_NASDAQ, pct))
plt.plot(pct_chg_thresholds, djia_pct_chg_days, color='blue', label='DJIA')
plt.plot(pct_chg_thresholds, sp500_pct_chg_days, color='green', label='S&P 500')
plt.plot(pct_chg_thresholds, nasdaq_pct_chg_days, color='red', label='NASDAQ')
plt.xlabel('Percentage Change Threshold Magnitude')
plt.ylabel('Number of Days')
plt.xlim(left=0.2, right=1.0)
plt.ylim(bottom=5, top=50)
plt.legend(loc='best')
plt.savefig('HW2 Task 4 Plot')
plt.close()


# Task 5: Calculate the 3-day simple moving average of a stock index.
def moving_average(stock_idx):
    """
    Generates a 1-D array containing the 3-day simple moving averages from the given array of stock indices.
    :param stock_idx: A 1-D array containing the values of a stock index
    :type stock_idx: numpy.ndarray
    :return moving_avg: A 1-D array containing the 3-day simple moving averages
    :rtype: numpy.ndarray
    """
    stock_idx = np.array(stock_idx)
    # Take the length of the original stock_idx array
    num_days = len(stock_idx)
    # Create the array 'moving_avg' that's 2 elements shorter than the original stock_idx array
    moving_avg = np.zeros(num_days - 2)
    # Calculate the 3-day simple moving average for each element in the stock index array. Slicing the array to
    # exclude the first and last two elements to ensure a 3-day window for the moving average calculation:
    # - stock_idx[:-2]: All elements except the last two.
    # - stock_idx[1:-1]: All elements except the first and last.
    # - stock_idx[2:]: All elements except the first two. Add corresponding elements from the sliced arrays and divide
    # by 3 to get the average.
    moving_avg[:] = (stock_idx[:-2] + stock_idx[1:-1] + stock_idx[2:]) / 3

    return moving_avg


# Task 6: Plotting the stock index and its 3-day moving average.
def plot_template(indices):
    """
    Set up a template for plotting stock index data with a three-day moving average
    :param indices: The name of the stock index for which the plot is being created.
    :type indices: str
    :return: none
    This function sets up the title and labels for the plot
    """
    plt.title('Three-Day Moving Average of ' + indices)
    plt.xlabel('Trading Days since Jun 1, 2016')
    plt.ylabel('Moving Average of Index')


# Plot for DJIA
plot_template('DJIA')
plt.plot(DAYS[2:], moving_average(DJIA), label='MA', color='blue')
plt.plot(DAYS[2:], DJIA[2:], label='Non-MA', color='green')
plt.legend(loc='best')
plt.savefig('HW2 Task 6 - DJIA')
plt.close()

# Plot for S&P 500
plot_template('S&P 500')
plt.plot(DAYS[2:], moving_average(STOCKS_SP_), label='MA', color='purple')
plt.plot(DAYS[2:], STOCKS_SP_[2:], label='Non-MA', color='orange')
plt.legend(loc='best')
plt.savefig('HW2 Task 6 - S&P 500')
plt.close()

# Plot for NASDAQ
plot_template('NASDAQ')
plt.plot(DAYS[2:], moving_average(STOCKS_NASDAQ), label='MA', color='red')
plt.plot(DAYS[2:], STOCKS_NASDAQ[2:], label='Non-MA', color='black')
plt.legend(loc='best')
plt.savefig('HW2 Task 6 - NASDAQ')
plt.close()
