import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("중학생_남자_키.xlsx")
# 히스토그램
# print(data[0:5])
# plt.hist(data, label='bins=5', bins=5)
# plt.legend()
# plt.show()
# plt.xlabel("height")
# plt.title("Histogram")
#
# plt.hist(data, label='bins=7', bins=7)
# plt.legend()
# plt.show()
#
# plt.hist(data, label='bins=10', bins=10)
# plt.legend()
# plt.show()
#
# plt.hist(data, label='bins=14', bins=14)
# plt.legend()
# plt.show()
#
# 막대 그래프
# x = [1,2,3,9,10,11]
# y = [16109, 41401, 53121, 59899, 53405, 82565]
#
# plt.bar(x,y, width=1)
# plt.show()

# 원그래프
# ratio = [22,24, 16,38] # 요소 수 / 전체 총합 의 비율을 표현해줌
# labels = ["pizza", "hamburger", "pasta", "chicken"]
# plt.pie(ratio, labels=labels, autopct="%.1f")
# plt.show()

# 선그래프
# x = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]
# y2 = [20.5, 21.0, 22.8, 23.6, 24.2, 24.3, 29.5
#
# plt.plot(x, y1, linestyle='solid', color='red', label='teens')
# plt.plot(x, y2, linestyle='dashed', color='orange', label='20s')
# plt.legend(loc='best', ncol=2)
# plt.show()

# import numpy as np
# boxplot
# data = pd.read_csv("스마트폰_이용시간.csv")
# print('median=', np.median(data))
# print('min=', np.min(data))
#
# plt.boxplot(y1, vert=False)
# plt.show()

# 산점도
# data = pd.read_excel("초등학생_키몸무게.xlsx" )
# print(data[0:5])
# print(data.height[0:5])
#
# plt.scatter(data.height, data.weight)
# plt.show()

# 3차원 seaborn

import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

sns.pairplot(iris, diag_kind='hist')
plt.show()