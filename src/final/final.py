import os

# 현재 스크립트의 디렉토리로 작업 디렉토리 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# import 
import matplotlib.pyplot as plt  # type: matplotlib.pyplot
import numpy as np
import pandas as pd
import scipy.stats as st
import seaborn as sns
from scipy.stats import chi2_contingency, chisquare
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

## 주석
# Tukey
# 매개변수로는 endog(첫자리)에 종속변수명 배열, 
# groups(두번째)에 독립변수명 배열을 넣어서 사용함


# 문제
