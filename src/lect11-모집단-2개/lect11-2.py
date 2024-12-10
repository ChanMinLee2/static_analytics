import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

# lect11-2 : 대응표본
data = pd.read_excel("./피트니스_결과.xlsx")
print(data.describe())

plt.boxplot([data.before, data.after], vert=False)
plt.show()

result = stats.ttest_rel(data.before, data.after, alternative='greater')
print(result)