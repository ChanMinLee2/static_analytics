import os

import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from statsmodels.formula.api import ols

# df = pd.read_excel("초등학교3학년_남자.xlsx")
# print(df.head())
#
# df.columns = ['height', 'weight']
# print(df.describe(), '\n')
#
# plt.scatter(df.height, df.weight)
# plt.xlabel('height')
# plt.xlabel('weight')
# plt.grid()
# plt.show()
#
# print(stats.pearsonr(df.height, df.weight))


# 현재 작업 디렉토리 출력
print("Current Working Directory:", os.getcwd())


df = pd.read_excel("Galtons Height Data_딸.xlsx")
df = df*2.54
print(df.describe(), '\n')

sns.regplot(x=df.father, y=df.daughter)
plt.show()

res = ols('df.daughter ~ df.father', data=df).fit()
print(res.summary())
print(stats.pearsonr(df.daughter, df.father))


