import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import chi2_contingency, chisquare

# 적합도 검정 - 관측값이 기대도수분포를 따르는지 분석 
obs_dice = [22, 19, 26, 25, 17, 11]
exp_dice = [20, 20, 20, 20, 20, 20] # 기대도수 분포

result = chisquare(f_obs=obs_dice, f_exp=exp_dice)
print(result)

# 독립성 검정 
obs = pd.DataFrame({'남':[26,20,11], '여':[10,15,18]})
obs.index=['만족','보통','불만족']
#      남   여 
# 만족   26  10
# 보통   20  15
# 불만족  11  18
result = chi2_contingency(obs, False)
print(result)

obs2 = pd.DataFrame({'남':[25,75], '여':[45,55]})
# obs2 = pd.DataFrame({'남':[35,65], '여':[40,60]}) -> PVALUE : 0.46 -> H0 채택 -> 결론 : 차이없다
obs2.index=['찬성', '반대']
result2 = chi2_contingency(obs2,False)
print(result2)

# 동질성 검정 = 독립성 검정인데 모집단 크기가 같아야함 

# data = pd.read_excel('test.xlsx')
# print(data)
# print(data.loc[0][1:], ) # row[1:]  # 첫 번째 값을 제외한 나머지
# df = pd.DataFrame({'oilhouse':np.repeat(['a','b','c'], repeats=3),
#                    'engine': ['engine1', 'engine2', 'engine3'] * 3 ,
#                    'distance':data.loc[0][1:].tolist() + data.loc[1][1:].tolist() + data.loc[2][1:].tolist(),
#                    })
# print(df)