import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import binom, norm
from matplotlib import pyplot as plt

# Q1,2 표준 정규 분포에서 다음의 확률을 계산
# Q1 : P(-1.26 <= Z <= 1.15)
mu = 0
sigma = 1

y1 = norm.cdf(-1.26, mu, sigma)
y2 = norm.cdf(1.15, mu, sigma)
Q1_answer = y2-y1
print(Q1_answer)

# Q2 : P(Z <= -2.5)
y3 = norm.cdf(-2.5, mu, sigma)
Q2_answer = y3
print(Q2_answer)

# Q3 : P(Z <= k) = 0.025 인 k 구하기
y4 = norm.ppf(0.025, mu, sigma)
k = y4 # Q3_answer = k
print(k)

# Q4, 5 확률 변수 X가 정규 분포 N(70, 3^2)를 따를 때, 다음의 확률을 계산
prev_mu = 70
prev_sigma = 3
prev_start = 70
prev_end = 76
# Q4 P(70 <= X <= 76)
# X를 Z로 표준화 진행 후 위 확률 표현은 다음과 같음 - P(0 <= Z <= 2)
# 표준화 후는 표준정규분포를 따르기 때문에 위 문제의 mu = 0, sigma = 1을 그대로 사용함
Z_start = (prev_start - prev_mu)/prev_sigma # 0
Z_end = (prev_end - prev_mu)/prev_sigma # 2
y5 = norm.cdf(Z_start, mu, sigma)
y6 = norm.cdf(Z_end, mu, sigma)
Q4_answer = y6-y5
print(Q4_answer)

# Q5 P(67 <= Z <= 73)
# X를 Z로 표준화 진행 후 위 확률 표현은 다음과 같음 - P(-1 <= Z <= 1)
# 표준화 후는 표준정규분포를 따르기 때문에 위 문제의 mu = 0, sigma = 1을 그대로 사용함
prev_start = 67
prev_end = 73
Z_start = (prev_start - prev_mu)/prev_sigma # 0
Z_end = (prev_end - prev_mu)/prev_sigma # 2
y7 = norm.cdf(Z_start, mu, sigma)
y8 = norm.cdf(Z_end, mu, sigma)
Q5_answer = y8-y7
print(Q5_answer)

