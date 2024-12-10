import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import pandas as pd
import scipy.stats as st
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 회귀분석 - cost에 따른 value의 변화를 회귀분석하라.
# H0 : 광고비와 결과값에는 유의미한 상관관계가 없다. H1 : 있다 

cost = [1, 2, 3, 4, 5]
value = [3, 4, 2, 5, 6]

df = pd.DataFrame({'cost': cost, 'value': value})
sns.regplot(x=df.cost, y=df.value)
plt.show()

res = ols('df.value ~ df.cost', data=df).fit()
print(res.summary())
print(st.pearsonr(df.cost, df.value))

# 결과에서 광고비 P>|t|가 0.188로 0.05 보다 크므로 H0를 채택하고, 광고비가 결과에 유의미한 영향을 끼치지 못함을 드러낸다.  
# 피어슨 상관계수도 0.7이지만 pvalue가 0.188로 나오기 때문에 H0를 채택하고, 이 상관관계가 유의미하지 않음을 드러낸다.