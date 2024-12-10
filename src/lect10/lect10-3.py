import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st

# data = pd.DataFrame(pd.read_excel("커피가격.xlsx"))
data = pd.read_excel("테이프길이.xlsx")
print(data.head(5))

print(data.describe())

# 단측검정 : H1 대립가설 - 테이프길이 평균은 80m보다 짧다, H0 귀무가설 - mu = 80
result = st.ttest_1samp(data, 80, alternative="less")
# -> pvalue = 0.015 <= 유의수준 = 0.05 -> 대립가설 H1 채택 (유의수준보다 더 작음), H0 기각
print(result)
# 결론: 유의수준 0.05 하에서 H1은 타당함.

# 양측검정 : H1 대립가설 - 테이프길이 평균은 80m이 아니다, H0 귀무가설 - mu = 80
result = st.ttest_1samp(data, 80)
# -> pvalue = 0.030 <= 유의수준 = 0.05 -> 대립가설 H1 채택 (유의수준보다 더 작음), H0 기각
print(result)

