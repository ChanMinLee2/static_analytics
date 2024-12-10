import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st

# data = pd.DataFrame(pd.read_excel("커피가격.xlsx"))
data = pd.read_excel("우유가격.xlsx")
print(data.head(5))

print(data.describe())

# 단측검정 : H1 가설 - 우유가격 평균은 1550보다 비싸다, H0 가설 - mu = 1550
result = st.ttest_1samp(data, 1550, alternative="greater")
# -> pvalue = 0.001 <= 유의수준 = 0.05 -> 귀무가설 H0 기각 (유의미한 수준에 미침), H1 채택
print(result)

# 결론 : 우유가격은 1550보다 비싸다는 주장은 타당하다.

# 양측검정 -> 가설 재정의 H1 가설 - 우유가격 평균은 1550이 아니다.
result = st.ttest_1samp(data, 1550, alternative='two-sided') # two-sided는 디폴트값임
# -> pvalue = 0.002 <= 유의수준 = 0.05 -> 귀무가설 H0 기각 (유의미한 수준에 미침)
print(result)