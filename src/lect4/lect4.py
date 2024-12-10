import pandas as pd
import numpy as np
from scipy import stats

# data = pd.read_excel('./Lecture4_data/중학생_남자_몸무게.xlsx')
# print(np.average(data)) #np method
# print(data.mean()) #pd method
# print("중앙값", data.median())
# print("최빈값", data.mode())
# test = [13,14,15,16,17]
# print(np.var(test, ddof=1)) # 불편 분산
# print(np.var(test)) # 표본 분산

data2 = pd.read_excel('./Lecture4_data/외식비.xlsx')
print(data2.describe())

# print(np.mean(data2, axis=0))
# print(np.max(data2, axis=0) - np.min(data2, axis=0))
# print(np.var(data2, axis=0))