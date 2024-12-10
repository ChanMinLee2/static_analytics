import numpy as np
import pandas as pd
from scipy import stats

## q1
## 50명이 수강한 파이썬 프로그래밍의 중간시험 시험성적이
## 기대보다 낮았다고 평가한 A교수는 중간시험 이후에 방과후 보충수업을 실시하였다.
## 기말시험 성적이 중간시험보다 나아졌는지에 대해 유의수준 5%하에서 검정하시오.

# 문제 : 대응표본, a보다 b가 커졌는지 (h1:a-b<0) 검정 -> ttest_ind(a,b, alternative='less')

# 파일 내용 불러오기
data1 = pd.read_excel("./hw-datas/1_파이썬 프로그래밍 성적.xlsx")
# 결과 변수에 대응표본(H1 : (mu_중간-mu_기말 < 0) (less)) ttest 결과 저장
result = stats.ttest_rel(data1.midterm, data1.final, alternative='less')
print("q1 pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q1 conclusion : H0 (귀무가설) 기각, 기말 성적이 향상됨\n")
else :
    print("q1 conclusion : H0 (귀무가설) 채택, 기말 성적이 향상되지 않음\n")



## q2
## 전화기용 보조배터리를 생산하는 A전기는 한국과 중국 두 곳에 생산공장을 운영하고 있다.
## 최근 중국에 전력공급이 원활하지 않아 생산된 제품의 질이 낮아졌을것으로 생각되어
## 두 곳에서 생산한 제품 표본에 대해 충전 후 지속시간을 비교하고자 한다.
## 한국공장에서는 85개를 중국공장에서는 100개의 제품에 대해 조사(2_배터리 지속시간.xlsx)하였고
## 두 공장 제품의 지속시간에 차이가있는지 유의수준 5%하에서 가설을 세우고 검정하시오.

# 문제 : 독립표본, 같은지 다른지 검정 -> ttest_ind(a,b, alternative='two-sided')

# 파일 내용 불러오기
data2 = pd.read_excel("./hw-datas/2_배터리 지속시간.xlsx")
d_china = data2.china
d_korea = data2.korea.dropna() # dropna를 사용해 필요 없는 86~100번째의 결측치를 제거함

result = stats.levene(d_china, d_korea, center='mean')
print("q2 levene pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q2 levene : H0 (귀무가설) 기각, 두 데이터는 등분산")
else :
    print("q2 levene : H0 (귀무가설) 채택, 두 데이터는 이분산")

# 결과 변수에 독립표본(H1 : (mu_중국-mu_한국 = 0) (two-sided)) ttest 결과 저장
result = stats.ttest_ind(d_china, d_korea, alternative='two-sided')
print("q2 pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q2 conclusion : H0 (귀무가설) 기각, 중국과 한국 제품 간의 지속시간 차이는 있다\n")
else :
    print("q2 conclusion : H0 (귀무가설) 채택, 중국과 한국 제품 간의 지속시간 차이는 없다\n")

# q3
# 규모와 종업원수가 비슷한 두 개의 생수공장을 운영하고 있는 A사는
# 두 공장에서 생산한 생수의 생산량이 같은지를 알기 위해 12개월 동안 조사했다.
# 조사한 결과(보조자료: 3_생수생산량)을 토대로 가설을 세우고 유의수준 5%하에서 가설을 검정하시오.

# 문제 : 독립표본, 같은지 다른지 검정 -> ttest_ind(a,b, alternative='two-sided')

# 파일 내용 불러오기
data3 = pd.read_excel("./hw-datas/3_생수생산량.xlsx", header=None)

# 원하는 행(row 3부터 row 15)과 열(대전공장, 대구공장) 선택
data3 = data3.iloc[4:15, :2]  # 4번째 행부터 끝까지, 첫 두 열만 선택
data3.columns = ["대전공장", "대구공장"]

# 숫자형으로 변환 후 변수에 할당
data3["대전공장"] = pd.to_numeric(data3["대전공장"])
data3["대구공장"] = pd.to_numeric(data3["대구공장"])
d_dj = data3["대전공장"]
d_dg = data3["대구공장"]

# 등분산 검정
result = stats.levene(d_dj, d_dg, center='mean')
print("q3 levene pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q3 levene : H0 (귀무가설) 기각, 두 데이터는 등분산")
else :
    print("q3 levene : H0 (귀무가설) 채택, 두 데이터는 이분산")

# 결과 변수에 독립표본(H1 : (mu_대전-mu_대구 = 0) (two-sided)) ttest 결과 저장
result = stats.ttest_ind(d_dj, d_dg, equal_var=False, alternative='two-sided' )
print("q3 pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q3 conclusion : H0 (귀무가설) 기각, 대전공장과 대구공장 간의 생산량 차이는 있다\n")
else :
    print("q3 conclusion : H0 (귀무가설) 채택, 대전공장과 대구공장 간의 생산량 차이는 없다\n")



# q4
# 직장인 전문 여론조사기관인 A리서치는 직장인들의 평균 점심비용(음료 제외)은 6,300원으로 조사되었고 발표하였다.
# 이에 구내식당이 없는 S기업 직원 중 100명을 대상으로 일주일간 점심비용의 평균을 조사한 결과(4_S기업 점심비용.xlsx)를
# 이용하여 A리서치가 발표한 내용에 대해 S기업의 조사결과와 차이가 있는지에 대해 유의수준 5%하에서 가설을 세우고 검정하시오.

# 문제 : n>30 표본 1개, 주어진 값과 같은지 다른지 검정 -> ttest_1samp(a,popmean=6300, alternative='two-sided')

data4 = pd.read_excel("./hw-datas/4_S기업 점심비용.xlsx")
mu=6300 # 기존에 추측되었던 모집단 평균

# 양측검정
result = stats.ttest_1samp(data4, mu, alternative='two-sided')
print("q4 pavlue :", result.pvalue)
if (result.pvalue < 0.05):
    print("q4 conclusion : H0 (귀무가설) 기각, A리서치 조사결과와 S기업 조사결과 간의 차이는 있다\n")
else :
    print("q4 conclusion : H0 (귀무가설) 채택, A리서치 조사결과와 S기업 조사결과 간의 차이는 없다\n")
