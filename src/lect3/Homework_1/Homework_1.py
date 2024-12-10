import math
import pandas as pd
import matplotlib.pyplot as plt

# matplot에서 한글 폰트 깨지는 이유로 폰트 변경
plt.rc('font', family='Malgun Gothic')  # Windows

# Q_1 - histogram
data_1 = [4, 8, 7, 4, 9, 5, 8, 8, 4, 3, 7, 2, 6, 6, 7, 6, 6, 4, 2, 4, 3, 1, 1, 6, 3, 5, 6, 5, 6, 5, 7, 5, 4, 5, 5, 3, 3]
sturges_formula_k = math.ceil(1 + math.log(len(data_1), 2))
plt.hist(data_1, label='vacation days', bins=sturges_formula_k )
plt.legend()
plt.show()

# Q_2 - boxplot
plt.boxplot(data_1, vert=False)
plt.show()  

# Q_3 - bar graph
lunch_menu_data = pd.read_csv("lunch_menu_data.csv")
menu_list = lunch_menu_data['메뉴'].tolist()
quantity_list = lunch_menu_data['수량'].tolist()
plt.bar(menu_list, quantity_list)
plt.show()

# Q_4 - pie chart
plt.pie(quantity_list, labels=menu_list, autopct='%.1f%%')
plt.legend(loc='upper left')
plt.show()

# Q_5 - line graph
year_price_data = pd.read_excel("year_price_data.xlsx")
year_list = year_price_data['년도'].tolist()
price_list = year_price_data['가격(원)'].tolist()
plt.plot(year_list, price_list)
plt.xlabel('년도')
plt.ylabel('가격(원)')
plt.show()