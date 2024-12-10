import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 세 가지 학습 방법(A, B, C)의 효과를 비교하려 합니다. 
# 각 방법에 대한 테스트 점수가 아래와 같을 때, 세 방법의 평균 점수에 유의미한 차이가 있는지 검정하세요.

A= [88, 92, 85, 87, 90]
B= [78, 81, 79, 83, 80]
C= [95, 92, 96, 94, 98]

# 일원 분산분석
print(f_oneway(A,B,C))

# 다중비교 (pvalue < alpha 일 때 여기까지, 차이가 있다면 어떤 케이스인지 알아내기)
# 왼쪽 col은 a,b,c 합쳐서 18개 아이템, 오른쪽 col은 'a' 6개 'b' 6개 'c' 6개
df = pd.DataFrame({'point':A+B+C, 'group':np.repeat(['A','B','C'], repeats=5)})
print(df)

# 매개변수로 넣을 때 endog=df['point'] 이렇게도 넣어짐 (매개변수 자리=값 형태)
result = pairwise_tukeyhsd(df['point'], df['group'], alpha=0.05)
print(result) # result의 reject는 H0(귀무)가설을 기각할 수 있는 지를 나타냄


# # 이원 분산분석 ( 반복없음 )
# df = pd.read_excel("./이원분석_주행거리.xlsx")
# model = ols('distance ~ C(road) + C(car)', data=df).fit()
# print(anova_lm(model)) # PR(>F)가 0.05보다 큰 지 작은 지 보면 됨
# # 결과적으로 car에 대해서는 H0 기각, road에 대해서는 H0 채택

# result = pairwise_tukeyhsd(df['distance'], df['car'], alpha=0.05)
# print(result) # b c는 차이없고 a는 b,c에 비해 대략 3.8정도 이득임

# df = pd.read_excel('./화장품_매출액.xlsx')
# df.columns = ['area', 'service', 'sales']

# sns.boxplot(x='area', y='sales', hue='service', data=df)
# plt.show()

# model = ols('sales ~ C(area) + C(service) + C(area):C(service)', data=df).fit()
# print(anova_lm(model)) # PR(>F)가 0.05보다 큰 지 작은 지 보면 됨

