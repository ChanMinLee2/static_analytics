import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

# 두 집단의 점수 현황 -> 집단 간 평균의 유의미한 차이가 있는 지 유의수준 5%로 분석 
# H0 : 집단 간 평균 차이는 없다, H1 : 집단 간 평균 차이는 있다.

A = [80, 85, 88, 90, 92]
B = [78, 83, 89, 91, 95]

data = pd.DataFrame({"A":A, "B":B})

plt.boxplot([data.A, data.B], vert=False)
plt.show()

result = stats.ttest_ind(data.A, data.B, alternative='two-sided')
print(result)

# pvalue = 0.957 > 0.05 이므로 H0 채택 , 따라서 두 집단 간 유의미한 평균 차이는 존재하지 않음