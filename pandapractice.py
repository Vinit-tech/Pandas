import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#_____________________________________________________________

"""Concatenating file"""


df = pd.read_csv('./Sales_Data/Sales_July_2019.csv')

files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()
for file in files:
    # print(file)
    df = pd.read_csv('./Sales_Data/' + file)
    all_months_data = pd.concat([all_months_data, df])
    # print(all_months_data)

all_months_data.to_csv('all_data.csv', index=False)

all_data = pd.read_csv('all_data.csv')


#____________________________________________________________

"""Cleaning Data"""

nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])



#_______________________________________________________________

"""What was the best month for sale? 
How much earned that month?"""



all_data['Months'] = all_data['Order Date'].str[0:2]

all_data['Months'] = all_data['Months'].astype('int32')

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

results = all_data.groupby('Months').sum()



"""PLoting Sales"""

Months = range(1,13)

#plt.bar(Months,results['Sales'])

#plt.xticks(Months)

#plt.xlabel('Months')
#plt.ylabel('Sales USD($)')
#plt.show()





"""What City had the highest number of sales?"""


#def get_city(address):
#    return address.split(',')[1]


all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1] + ' ' + x.split(',')[2].split(' ')[1])   #-"OR"- x.split --> get_city(x)

results = all_data.groupby('City').sum()

cities = [city for city, df in all_data.groupby('City')]

#plt.bar(cities, results['Sales'])
#plt.xticks(cities,rotation='vertical', size=8)
#plt.xlabel('Cities')
#plt.ylabel('Sales')
#plt.show()



"""What time we should we display advertisement to maximise likelihood of customers buying product"""

all_data['Hour'] = all_data['Order Date'].apply(lambda y: y.split(' ')[1].split(':')[0])

results = all_data.groupby('Hour').count()

Hour = [hour for hour, df in all_data.groupby('Hour')]

# plt.plot(Hour, results['Sales'])
# plt.grid()
# plt.xlabel('Hour')
# plt.ylabel('Sale')
# plt.show()


"""What Products are  often Sold together"""


# all_data.groupby('Order ID').count()

df1 = all_data[all_data['Order ID'].duplicated(keep=False)]

df1['Grouped'] = df1.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df1 = df1[['Order ID', 'Grouped']].drop_duplicates()


# print(all_data.head(10))














"""PROBLEM ONE"""
# df = pd.DataFrame(np.random.random(size=(5, 3)))
#
# for i in df:
#     mean = df.iloc[i].mean()
#     for j in df.iloc[i]:
#         row = j - mean
#         df = df.replace([j], row, regex=True)
#
#
# print(df)

"""PROBLEM TWO"""

# df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

# df = pd.DataFrame([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# for column in df:
#     columns = df.sum()
#     df.loc['row'] = columns
#
# print(df)

'''PROBLEM THREE'''
# df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
#                    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
#
# df['a'] = df.loc[df['grps'] == 'a']
# print(df)
