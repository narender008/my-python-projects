import numpy as np
from numpy import genfromtxt
from currency_converter import CurrencyConverter

filename = (
    "/Users/narender/Projects/python/numpy/WK1_Airbnb_Amsterdam_listings_proj.csv"
)
my_data = genfromtxt(filename, delimiter="|", dtype="unicode")

print(my_data)
