import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

food_data = pd.read_csv('C:/Users/User/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')
df = pd.DataFrame(food_data)
df.info()

y = [(2, 4), (7, 8), (1, 5, 9)]
x = y[1][1]
print(x)

print(df.shape)

lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]
col = ['Age','Nationality','Overall']

df1 = pd.DataFrame(lst, columns=col, index=[1,2,3])
print(df1)

S = [['him', 'sell'], [90, 28, 43]]
print(S[0][1][1])

total = df.groupby(['Area', 'Element'])['Y2015'].sum().loc['Madagascar', 'Protein supply quantity (g/capita/day)']
print(total)     

total1 = df.groupby('Area')['Y2017'].sum().sort_values()
print(total1)     

columns = ['Element Code', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']
df2 = food_data[columns]
correlations = df2.corr()['Element Code'][1:]
least_corr_year = correlations.abs().idxmin()
print(f"The year with the least correlation with 'Element Code' is: {least_corr_year}")

total1 = df.groupby('Element')[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].sum()
print(total1) 

mean = round(df['Y2017'].mean(), 2)
print(mean)

std = round(df['Y2017'].std(), 2)
print(std)

total3 = df.groupby('Item')[['Y2015', 'Y2018']].sum().loc['Wine']
print(total3)

total_countries = df['Area'].nunique()
print(total_countries)

array  = np.array([[94, 89, 63], [93, 92, 48], [92, 94, 56]])
print(array[:2, 1:])

