# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:12:29 2022

@author: dj
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solution(filename,countries,columns,indicator):
    '''
    

    Parameters
    ----------
    filename : string
        filename.
    countries : list
        list of countries to be considered.
    columns : list
        list of countries to be used.
    indicator : string
        indicator to be retrieved from the dataset.

    Returns
    -------
    df : pandas dataframe
        original dataframe.
    dataframe
        transposed datframe.

    '''
    df = pd.read_csv(filename,skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries]
    df = df.loc[countries]
    return df,df.transpose()


filename = 'API_19_DS2_en_csv_v2_4700503.csv'
countries =['Belgium','Canada','Brazil','Colombia','Nigeria']
columns = ['Country Name', '2005','2006','2007','2008','2009','2010','2011','2012']
indicators = ['Urban population', 'Electric power consumption (kWh per capita)']

cnty_urban, year_urban = solution(filename,countries,columns,indicators[0])
cnty_electric, year_electric = solution(filename,countries,columns,indicators[1])

#Line plot
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_urban.index,year_urban[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the Urban Population for these 5 countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.savefig('urban poplation.png')
plt.show()

#bar plot
cnty_electric.plot(kind='bar')
plt.title('Grouped bar for electric consumption for different countries over the years')
plt.xlabel('Countries')
plt.ylabel('electric consumption')
plt.savefig('urban poplation 2.png')
plt.show()

#heat maps showing correlation
canada = pd.DataFrame(
{'Urban Population': year_urban['Canada'],
'Elec. consumption': year_electric['Canada']},
[ '2005','2006','2007','2008','2009','2010','2011','2012'])

plt.figure(figsize=(8,5))
sns.heatmap(canada.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap Canada')
plt.savefig('urban and poplation.png')
plt.show()