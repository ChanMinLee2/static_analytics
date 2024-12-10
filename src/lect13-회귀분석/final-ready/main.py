import os

import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from statsmodels.formula.api import ols

print(os.getcwd())

x = [89,	91,	73,	80,	94,	100,	79,	90]
y = [3.69,	4.08,	3.43,	3.69,	4.32,	4.5,	3.57,	4.21]

df = pd.DataFrame({'point': x, 'gpa': y})
sns.regplot(x=df.point, y=df.gpa)
plt.show()

res = ols('df.gpa ~ df.point', data=df).fit()
print(res.summary())
print(stats.pearsonr(df.point, df.gpa))

# 회귀식 : intercept + df.gpa-coef * gpa => y = 3.8254 + 21.13 * x
# 결론 : x와 y는 유의미한 음의 상관관계를 가진다 