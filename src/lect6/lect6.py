import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import binom, norm
from matplotlib import pyplot as plt
import scipy.stats as st

mu = 0
sigma = 1

point = norm.ppf(0.9, mu, sigma)
point2 = norm.ppf(0.6915, mu, sigma)

y1 = norm.cdf(0.5, mu, sigma)
y2 = norm.cdf(-1.5, mu, sigma)

print(point)
print(point2)
# print(y1)
# print(y2)
# print(y1-y2)