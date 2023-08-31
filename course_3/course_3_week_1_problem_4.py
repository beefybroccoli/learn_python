import csv
from matplotlib import pyplot as plt

file = open('natural_gas_futures_weekly_all.csv','r')
csv_handle = csv.DictReader(file)

weekly_prices = []
dates = []

for rows in csv_handle:
    dates.append(rows['Date'])
    weekly_prices.append(0.5 * (float(rows['High']) + float(rows['Low'])) )
file.close()

plt.plot(range(len(weekly_prices)), weekly_prices, '-b')
plt.xlabel('Week #')
plt.ylabel('Crude Oil Future Price')
plt.autoscale
plt.show()

"""
First we compute the fast fourier transform of the data using `numpy.fft.fft` function. Note that length of fft is also 1081.
Let the fft be stored in list `fft_data`.

Second, create a list called frequencies that has the frequency corresponding to each element in the `fft_data`. Remember that the data's time period is 1 week. We will represent all frequencies in the unit $\text{week}^{-1}$.

Using a combination of the `numpy.fft.fft` and `numpy.fft.ifft` functions, please extract the low frequency components of the signal that correspond to frequencies in the range `[0, 1/52 weeks]`, `[1/52 weeks, 1/13 weeks]` and the high frequency terms greater than or equal to  `1/13` weeks. 

The resulting lists should be called : `upto_1_year`, `one_year_to_1_quarter` and `less_than_1_quarter` respectively.
"""

from numpy.fft import fft, ifft
from numpy import real,imag

# here we have computed the fft of the weekly_prices
fft_data =  fft(weekly_prices)
N = len(fft_data)
assert(N == len(weekly_prices))
# TODO: first fill in the frequencies call this list 
# fft_frequencies -- it must have length N
# it must store the frequencies of each element in the fft_data
# ensure that the frequencies of the second half are negative.
# your code here

# This function will be useful for you. Please go through the code.

def select_all_items_in_freq_range(lo, hi):
    # TODO: go through the fft_data and select only those frequencies in the range lo/hi
    new_fft_data = [] # make sure we have the 0 frequency component
    for (fft_val, fft_freq) in zip(fft_data, fft_frequencies):
        if lo <= fft_freq and fft_freq < hi:
            new_fft_data.append(fft_val)
        elif -hi < fft_freq and fft_freq <= -lo:
            new_fft_data.append(fft_val)
        else:
            new_fft_data.append(0.0)
    filtered_data = ifft(new_fft_data)
    assert all( abs(imag(x)) <= 1E-10 for x in filtered_data)
    return [real(x) for x in filtered_data]

upto_1_year = [] # All signal components with frequency < 1/52
one_year_to_1_quarter = [] # All signal components with frequency between 1/52 (inclusive) and 1/13 weeks (not inclusive)
less_than_1_quarter = [] # All signal components with frequency >= 1/13 

# TODO: Redefine the three lists using the select_all_items function
# your code here
# -----------------------------------------------------------------