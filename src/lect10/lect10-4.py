import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st
import numpy as np

# data = pd.DataFrame(pd.read_excel("커피가격.xlsx"))
sample = [50.3, 49.5, 49.7,  51.1, 50.2 , 51, 51, 48.7, 51, 51.2]
data = pd.DataFrame({
    'C0' : sample,
})

print(data.head(5))
print(data.describe())

# 단측검정 : H1 가설 - 휴지길이 평균은 50m보다 길다, H0 가설 - mu = 50
result = st.ttest_1samp(data, 50, alternative="greater")
# -> pvalue = 0.099 >= 유의수준 = 0.05 -> 귀무가설 H0 채택 (유의미한 수준에 못 미침), H1 기각
print(result)
# 결론: 유의수준 0.05 하에서 H1은 타당하지 않다.

# 양측검정 : H1 가설 - 휴지길이 평균은 50m가 아니다, H0 가설 - mu = 50
result = st.ttest_1samp(data, 50)
# -> pvalue = 0.198 >= 유의수준 = 0.05 -> 귀무가설 H0 채택 (유의미한 수준에 못 미침), H1 기각
print(result)
