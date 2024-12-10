import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st
import numpy as np

# data = pd.DataFrame(pd.read_excel("커피가격.xlsx"))
data = pd.read_excel("커피가격.xlsx")
print(data.head(5))

print(data.describe())

result = st.ttest_1samp(data, 3055, alternative="greater")
# 정규분포로 구한 pvalue 0.3594 (별 차이 없음 그냥 t분포씀)
# -> pvalue = 0.3596 >= 유의수준 0.05 => 귀무가설 채택 (유의미한 수준에 미치지 못함)
print(result)

# 양측검정 (pvalue 두배)
result = st.ttest_1samp(data, 3055)
# -> pvalue = 0.3596 >= 유의수준 0.05 => 귀무가설 채택 (유의미한 수준에 미치지 못함)
print(result)

# plt.hist(data, bins=7)
# plt.show()

#결론 : 평균 커피값은 3055보다 비싸지 않다