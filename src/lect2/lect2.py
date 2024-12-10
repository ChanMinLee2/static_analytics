import numpy as np # 수학적인 연산을 적용할 수 있도록, 같은 자료형을 여러개 관리하는 자료구조 사용 (array)
import pandas as pd
import openpyxl as opxl

file_data1 = pd.read_csv("./datas/sample1.csv")
file_data2 = pd.read_csv("./datas/sample2.txt", encoding='cp949')
file_data3 = pd.read_csv("./datas/sample3.txt", sep='\t',encoding='euc-kr')
file_data4 = pd.read_excel("./datas/sample4.xlsx")
print(file_data1, file_data2, file_data3, file_data4)
