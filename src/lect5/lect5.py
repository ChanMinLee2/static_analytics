import pandas as pd
import numpy as np
from scipy.stats import binom, norm
from matplotlib import pyplot as plt

n= 5
x = np.arange(n+1)
print(x)

mean, var = binom.stats(n,0.5)
print(mean)
print(var)

prob = binom.pmf(x,n,0.5)
print(prob)

prob = binom.pmf(2,n,0.5)
print(prob)

mu = 50
scale = 5
x =np.arange(mu-30, mu+30, 0.1)
y = norm.pdf(x, mu, scale)

plt.bar(x,y)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.show()