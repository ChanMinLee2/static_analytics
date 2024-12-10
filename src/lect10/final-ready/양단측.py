import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st

# q1, H0 : 평균 음료 용량은 500미만이다, H1 : 이상이다
data1 = [503.49, 501.58, 503.94, 506.57, 501.30, 501.30, 506.74, 504.30, 500.59, 503.63, 500.61, 500.60, 502.73, 496.26, 496.83, 500.31, 498.96, 502.94, 499.28, 497.76]

data1 = pd.DataFrame(data=data1)
print(data1.describe())

result = st.ttest_1samp(data1, 500, alternative="greater")
print(result)
# pvalue -> 0.016 -> H0 기각 -> 평균 음료 용량은 500ml 이상이라고 볼 수 있다.

# q2, H0 : 평균 근무시간이 8.2시간이다 , H1 아니다 
data2 = [8.86, 7.81, 8.04, 7.70, 7.66, 7.48, 8.48, 8.35, 7.39, 8.31, 8.54, 9.14, 8.68, 8.25, 7.96]
data2 = pd.DataFrame(data2)
print(data2.describe())

result2 = st.ttest_1samp(data2, 8.2, alternative="two-sided")
print(result2) # pvalue 0.86 > 0.05 => H0 채택 -> 평균 근무시간이 8.2시간이다. 
