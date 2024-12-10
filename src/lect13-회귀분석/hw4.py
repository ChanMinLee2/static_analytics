import os

import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 현재 스크립트의 디렉토리로 작업 디렉토리 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('===============q1===================')
# q1 3개 정유사에 대한 무연휘발유와 3가지 종류의 엔진에 대해 주행거리(km)를 측정한 결과는 다음과 같다.
# 주행거리에 있어서 무연휘발유 효과와 엔진 효과에 대해 유의수준 5%하에서 검정하시오.
# 만일 차이가 있다면 어떤 것과 어떤 것이 차이가 있는지를 다중비교를 통해 밝히시오.

# q1 데이터
data1 = pd.read_excel("q1.xlsx")

# q1 데이터를 선형회귀모델에 넣은 결과를 anova로 검사함
model = ols('distance ~ C(oilhouse) + C(engine)', data=data1).fit()
print("anova-------------------------------")
print(anova_lm(model) , '\n')

# 위 anova 결과에 따라 H0가 기각된 engine에 대해서만 다중비교 시행
print("tukeyhsd----------------------------")
result = pairwise_tukeyhsd(data1['distance'], data1['engine'], alpha=0.05)
print(result , '\n')

print('===============q2===================')
# q2 아래 연도별 평균기온와 강수량 데이터를 이용하여 회귀분석을 실시하고, 결과를 해석하시오.
#(1) 상관계수는 얼마인가?
#(2) 선형 회귀분석 결과 평균기온(x)에 따른 강수량(y)의 회귀식을 도출하시오.

# q2 데이터
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
temp = [12.7, 12.8, 12.9, 12.8, 13.3, 12.1, 13, 13.3, 12.9, 12.9, 12.1, 12, 12.2, 12.5, 13.4, 13.6, 13.6, 13, 12.9, 13.5]
rain = [1186.8, 1386, 1388, 2012, 1499.1, 1358.4, 1681.9, 1212.3, 1356.3, 1564, 2043.5, 2039.3, 1646.3, 1403.8, 808.9, 792.1, 991.7, 1233.2, 1284.1, 891.3]

# q2 데이터를 zip으로 데이터 프레임화
data2 = pd.DataFrame(zip(year, temp, rain))
data2.columns = ['year', 'temp', 'rain']
# print(data2)

# ols 선형회귀모델에 데이터 넣은 결과 출력
print("ols---------------------------------")
res = ols('rain ~ C(temp)', data=data2).fit()
print(res.summary(), '\n')
# res = ols('data2.rain ~ data2.temp', data=data2).fit()
# print(res.summary(), '\n')

# 피어슨 상관계수 구하기
print("pearson-----------------------------")
print(stats.pearsonr(data2.temp, data2.rain), '\n')
# print(stats.pearsonr(data2.rain, data2.temp), '\n')

# 상관계수 : -0.733486631411419
# 회귀식 : y = 14.2363 - 0.001x
print("result-----------------------------")
# print('상관계수 :', -0.733486631411419)
# print("회귀식 : y = 14.2363 - 0.001x")