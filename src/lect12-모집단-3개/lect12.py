import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 현재 스크립트의 디렉토리로 작업 디렉토리 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

a = [25,29,27,23,22,25]
b = [34,36,38,32,35,35]
c = [29,31,27,26,25,27]

# 일원 분산분석
print(f_oneway(a,b,c))

# 다중비교 (pvalue < alpha 일 때 여기까지, 차이가 있다면 어떤 케이스인지 알아내기)
# 왼쪽 col은 a,b,c 합쳐서 18개 아이템, 오른쪽 col은 'a' 6개 'b' 6개 'c' 6개
df = pd.DataFrame({'product':a+b+c, 'group':np.repeat(['a','b','c'], repeats=6)})
print(df)

# 매개변수로 넣을 때 endog=df['product'] 이렇게도 넣어짐 (매개변수 자리=값 형태)
result = pairwise_tukeyhsd(df['product'], df['group'], alpha=0.05)
print(result) # result의 reject는 H0(귀무)가설을 기각할 수 있는 지를 나타냄

# 결과 : a-b, b-c 관계는 reject -> H0 기각됨 -> a,b b,c는 유의미한 표준평균 차이를 보임


# 이원 분산분석 ( 반복없음 )
df = pd.read_excel("./이원분석_주행거리.xlsx")
model = ols('distance ~ C(road) + C(car)', data=df).fit() # distance가 종속변수임 
print(anova_lm(model)) # PR(>F)가 0.05보다 큰 지 작은 지 보면 됨 -> PR(F)가 0.05보다 작으면 H0(종속변수에의 영향 x인 가설) 기각 
# 결과적으로 car에 대해서는 H0 기각, road에 대해서는 H0 채택

result = pairwise_tukeyhsd(df['distance'], df['car'], alpha=0.05)
print(result) # b c는 차이없고 a는 b,c에 비해 대략 3.8(meandiff)정도 이득임


# 이원 분산분석 ( 반복있음 )
df = pd.read_excel('./화장품_매출액.xlsx')
df.columns = ['area', 'service', 'sales']

# sns.boxplot(x='area', y='sales', hue='service', data=df)
# plt.show()

model = ols('sales ~ C(area) + C(service) + C(area):C(service)', data=df).fit()
print(anova_lm(model)) # PR(>F)가 0.05보다 큰 지 작은 지 보면 됨

result = pairwise_tukeyhsd(df["sales"], df["area"])
print(result)
