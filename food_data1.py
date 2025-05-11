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

#code output
<class 'pandas.core.frame.DataFrame'>     
RangeIndex: 60943 entries, 0 to 60942     
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Area Code     60943 non-null  int64  
 1   Area          60943 non-null  object 
 2   Item Code     60943 non-null  int64  
 3   Item          60943 non-null  object 
 4   Element Code  60943 non-null  int64
 5   Element       60943 non-null  object
 6   Unit          60943 non-null  object
 7   Y2014         59354 non-null  float64
 8   Y2015         59395 non-null  float64
 9   Y2016         59408 non-null  float64
 10  Y2017         59437 non-null  float64
 11  Y2018         59507 non-null  float64
dtypes: float64(5), int64(3), object(4)
memory usage: 5.6+ MB
8
(60943, 12)
   Age Nationality  Overall
1   35    Portugal       94
2   33   Argentina       93
3   30      Brazil       92
e
173.05
Area
Sudan (former)                       0.00
Ethiopia PDR                         0.00
Comoros                             59.84
Seychelles                         442.34
Sao Tome and Principe            12662.63
Cabo Verde                       14650.74
Guinea-Bissau                    19102.77
Lesotho                          21267.96
Botswana                         22101.30
Djibouti                         22729.91
Gambia                           23154.18
Gabon                            27979.64
Liberia                          29342.20
Namibia                          29874.89
Central African Republic         29937.00
Congo                            41181.68
Togo                             49841.88
Mauritius                        51114.83
Eswatini                         54343.33
Sierra Leone                     55311.33
Chad                             71594.68
Rwanda                           73663.69
Zimbabwe                         75919.34
Senegal                          95681.15
Guinea                           98138.87
Burkina Faso                    101855.07
Zambia                          103223.77
Tunisia                         124167.20
Benin                           124771.22
Niger                           126707.58
Madagascar                      131197.73
Mali                            149928.33
Mauritania                      156665.46
Mozambique                      161407.98
Malawi                          181098.71
Uganda                          213950.38
Côte d'Ivoire                   224599.01
Angola                          229159.57
Cameroon                        232030.43
Sudan                           239931.92
Kenya                           264660.66
United Republic of Tanzania     322616.85
Algeria                         325644.27
Ghana                           337599.06
Morocco                         388495.36
Ethiopia                        448683.76
South Africa                    517590.54
Egypt                           866379.92
Nigeria                        1483268.23
Name: Y2017, dtype: float64
The year with the least correlation with 'Element Code' is: Y2016
                                             Y2014       Y2015       Y2016       Y2017       Y2018
Element
Domestic supply quantity                1996716.35  2021493.55  2044842.70  2088198.10  2161192.10
Export Quantity                          150020.64   157614.47   151920.46   182338.80   181594.80
Fat supply quantity (g/capita/day)        10225.56    10235.74    10102.77    10253.84    10258.69
Feed                                     216927.89   225050.22   228958.65   223705.68   233489.68
Food                                    1212332.49  1232361.10  1247022.17  1258888.28  1303841.28
Food supply (kcal/capita/day)            454257.00   453383.00   451810.00   454681.00   455261.00
Food supply quantity (kg/capita/yr)       49650.63    49345.13    48985.28    48690.04    49056.85
Import Quantity                          274144.48   267018.46   286582.78   294559.09   287997.09
Losses                                   153223.00   155439.00   157787.00   160614.00   163902.00
Other uses (non-food)                     78718.13    66254.41    69563.68    91645.97    91300.97
Processing                               282923.00   287929.00   280631.00   292836.00   308429.00
Production                              1931287.75  1947019.39  1943537.15  2030056.89  2075072.89
Protein supply quantity (g/capita/day)    11836.46    11833.95    11779.69    11842.45    11833.56
Residuals                                 30149.00    30045.00    37224.00    35500.00    34864.00
Seed                                      21922.92    23976.82    23389.20    24870.14    25263.14
Stock Variation                           58749.83    34910.99    33140.12    54316.91    20577.91
Total Population - Both sexes           1031585.00  1058081.00  1085107.00  1112641.00  1140605.00
Tourist consumption                         416.00      349.00       89.00       91.00       90.00
140.92
1671.86
Y2015    4251.81
Y2018    4039.32
Name: Wine, dtype: float64
49
[[89 63]
 [92 48]]
PS C:\Users\User\python> 
