import numpy as np
import pandas as pd
from scipy import stats

# lect11-1 : 독립표본
# 사례수가 다른 경우가 일반적이므로 각각 다른 변수로 데이터를 불러들여서 사용하는 게 좋음

# 꼭 기억하자.
# p value는 "분포그래프 상, 이번 분석에서 구해진 유의수준 영역의 크기(확률)"를 나타낸다
# 유의수준은 분포 그래프 상 정해진 크기(확률)이다.
# 양측검정에서 p가 유의수준보다 작다 : 새로 구해본 유의수준이 기존 유의수준을 깨트림(이번게 평균으로부터 더 멀어짐) -> 귀무 기각

data = pd.read_excel("./대학생_수면시간.xlsx")
print(data.describe())

# from matplotlib import pyplot as plt
# plt.boxplot([data.male, data.female.dropna()], vert=False)
# plt.show()

d1 = pd.read_excel("./대학생_수면시간_남자.xlsx")
d2 = pd.read_excel("./대학생_수면시간_여자.xlsx")
d3 = pd.read_excel("./성인_스마트폰_이용시간_남자.xlsx")
d4 = pd.read_excel("./성인_스마트폰_이용시간_여자.xlsx")
result = stats.levene(d1.male, d2.female, center='mean')
print(result) # pvalue < 0.05, 즉 귀무가설 기각 -> 이분산
result = stats.levene(d3.male, d4.female, center='mean')
print(result) #0.49 > 0.05, 즉 귀무가설(두 분산이 같다) 채택 -> 등분산