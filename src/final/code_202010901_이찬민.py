import os

# import 
import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import numpy as np
import pandas as pd
import scipy.stats as st
import seaborn as sns
from scipy.stats import chi2_contingency, chisquare, f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 현재 스크립트의 디렉토리로 작업 디렉토리 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# excel_name = "data_num_name.xlsx"
excel_name = "data_202010901_이찬민.xlsx"


# Q1 code here
df1 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q1")

# 각 라인별 결함부분
line1 = [11, 28, 44, 17]
line2 = [25, 31, 34, 10]
line3 = [27, 15, 42, 16]
# 일원 분산분석
print(f_oneway(line1, line2, line3))

# Q2 code here
df2 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q2")
result = st.ttest_1samp(df2, 55000, alternative="greater")
print("q2", result) # pvalue : 0.27972152 -> H0 채택
# 56300?

# Q3 code here
df3 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q3")
# 작년점수 75점보다 유의미한 변화가 있었는지
result = st.ttest_1samp(df3, 75, alternative="two-sided")
print("q3",result) # pvalue : 0.18374569 -> H0 채택
# 77.72


# Q4 code here
df4 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q4")
# 이원 분산분석 ( 반복없음 )
model = ols('매출 ~ C(영업부) + C(분기)', data=df4).fit()
print(anova_lm(model))  
# 영업부만 다중비교
result = pairwise_tukeyhsd(df4['매출'], df4['영업부'], alpha=0.05)
print(result) 


# Q5 code here
df5 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q5")
# 독립표본 ttest
result = st.ttest_rel(df5["기존 키보드"], df5["새 키보드"], alternative='two-sided')
print("q5", result)
# 45.40833333	51.96666667



# Q6 code here
df6 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q6")

# 이원 분산분석 ( 반복있음 )
model = ols('당도 ~ C(비료) + C(과일) + C(비료):C(과일)', data=df6).fit()
print(anova_lm(model)) 
# 당도와 비료 다중비교
result = pairwise_tukeyhsd(df6["당도"], df6["비료"])
print(result)
# 당도와 과일 다중비교
result = pairwise_tukeyhsd(df6["당도"], df6["과일"])
print(result)



################### Put your final exam answer here #####################################
# 1번 정답
# 가설 1
# H0: 생산라인별로 결함부분에 차이가 없다.
# H1: 생산라인별로 결함부분에 차이가 있다.
# p값 : 
  # 가설 1 : 1.000000
# 기각여부 :
  # 가설 1 : H0 채택
# 결론 : 
# 결론에 앞서 다중비교 진행 
  # 따라서 결론은, 유의수준 5% 하에서, 생산 라인 간 결함부분에 유의미한 차이는 없다.

# 2번 정답
# 가설
# H0: 수원지역 성인 기준 월 휴대전화 사용요금이 55000원이다.
# H0: 수원지역 성인 기준 월 휴대전화 사용요금이 55000원 이상이다.
# p값 : pvalue : 0.27972152 
# 기각여부 : H0 채택
# 결론 : 수원지역 성인 기준 월 휴대전화 사용요금은 유의수준 5%수준 하에서, 55000원이 맞다.

# 3번 정답
# 가설
# H0: 보충학습 후에도 영어성적이 75점이다 (좋아지거나 나빠지지 않았다)
# H1: 보충학습 후에 영어성적이 달라졌다. (좋아지거나 나빠졌다)
# p값 : pvalue : 0.18374569 
# 기각여부 : H0 채택
# 결론 : 유의수준 5% 하에서, 보충학습 후에도 영어 성적이 75점이 유의미한 차이는 없다. 

# 4번 정답
# 가설 1
# H0: 부서별로 실적에 차이가 없다. 
# H1: 부서별로 실적에 차이가 있다.
# 가설 2
# H0: 분기별로 실적에 차이가 없다. 
# H1: 분기별로 실적에 차이가 있다.
# p값 
#   가설 1 (부서) pvalue : 0.008998
#   가설 2 (분기) pvalue : 0.278080
# 기각여부 :
  # 가설 1 : H0 기각
  # 가설 2 : H0 채택
# 결론 :
  # 결론에 앞서 부서 다중비교 진행 
  # =========================================================
  # group1 group2 meandiff p-adj    lower      upper   reject
  # ---------------------------------------------------------
  #      A      B    340.0 0.7315  -509.3383 1189.3383  False
  #      A      C   -685.0 0.1452 -1534.3383  164.3383  False
  #      A      D    337.5 0.7365  -511.8383 1186.8383  False
  #      A      E    305.0 0.7994  -544.3383 1154.3383  False
  #      B      C  -1025.0 0.0148 -1874.3383 -175.6617   True
  #      B      D     -2.5    1.0  -851.8383  846.8383  False
  #      B      E    -35.0 0.9999  -884.3383  814.3383  False
  #      C      D   1022.5 0.0151   173.1617 1871.8383   True
  #      C      E    990.0 0.0189   140.6617 1839.3383   True
  #      D      E    -32.5    1.0  -881.8383  816.8383  False
  # ---------------------------------------------------------
# 따라서 결론은 유의수준 5%하에서, 분기간 실적차이는 없고 부서별로는 (B-C, C-D, C-E) 세 케이스에서 차이가 발생했다.

# 5번 정답
# 가설
# H0: 새로운 키보드와 기존 키보드의 분당 단어수는 똑같다.
# H1: 새로운 키보드는 기존 키보드의 분당 단어수와 비교하여 증가했다.
# p값 : 0.02827182262689341
# 기각여부 : H0 채택 (유의수준 1%)
# 결론 : 유의수준 1% 하에서, 새로운 키보드와 기존 키보드의 분당 단어수는 유의미한 차이는 없다.

# 6번 정답
# 가설 1
# H0: 비료에 따라 당도에 차이가 없다
# H1: 비료에 따라 당도에 차이가 있다.
# 가설 2
# H0: 과일에 따라 당도에 차이가 없다
# H1: 과일에 따라 당도에 차이가 있다.
# 가설 3
# H0: 과일과 비료간의 교호작용이 없다
# H1: 과일과 비료간의 교호작용이 있다
# p값
  # 가설 1 : 5.226182e-12
  # 가설 2 : 1.038730e-15
  # 가설 3 : 6.699647e-05
# 기각여부 : 세 가설 모두 H0이 기각된다.
# 결론 : 
  # 결론에 앞서 다중비교 진행 
  # 1. 비료 다중비교
  # Multiple Comparison of Means - Tukey HSD, FWER=0.05
  # ===================================================
  # group1 group2 meandiff p-adj   lower  upper  reject
  # ---------------------------------------------------
  #   비료 A   비료 B   0.2111  0.966 -1.8913 2.3136  False
  #   비료 A   비료 C      2.2 0.0391  0.0975 4.3025   True
  #   비료 B   비료 C   1.9889 0.0662 -0.1136 4.0913  False
  # ---------------------------------------------------
  # 2. 과일 다중비교
  # Multiple Comparison of Means - Tukey HSD, FWER=0.05
  # ==================================================
  # group1 group2 meandiff p-adj  lower  upper  reject
  # --------------------------------------------------
  #    복숭아     수박   2.6667 0.0002 1.3026 4.0308   True
  #    복숭아     포도   3.8778    0.0 2.5137 5.2419   True
  #     수박     포도   1.2111 0.0885 -0.153 2.5752  False
  # --------------------------------------------------
# 따라서 결론은 유의수준 5%하에서, (비료 별로, 과일종류 별로) 모두 당도 차이가 발생했다.
# 비료는 A-C 비료간에서 차이가 발생했고, 과일종류는 복숭아-수박, 복숭아-포도 간 당도 차이가 발생했다. 
# 또한 비료와 과일종류간에는 교호작용이 존재한다.
