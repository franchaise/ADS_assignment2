# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:19:11 2022

@author: Lenovo
"""
''' Data Analysis of CLimate Change based on the data source provided by World bank'''

#Importing python libraries to carry out data importation, sorting, analysis and presentation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#setting display to show rows and column for easy readability
pd.set_option('max_rows', 63)
pd.set_option('max_columns', 10)

#Creationof function to read and transpose data
def file_read_transpose_csv(input_file,country_name,column_name,criterion):
    """read and transposes a csv file, returning both the original file and the transpose file,
    with header provided for transpose file.
    skiprows: used to remove first three line rows within the DataFrame
    input_file: file to be read    
    Country_name :column bearing 'Country name'
    column_name = list of columns within the dataframe
    Criterion : list of indicators to work with
    WB_data: name of the dataframe
     """
     
    WB_data = pd.read_excel(input_file, skiprows = 3)
    #Filtering indicator Name
    WB_data =WB_data[WB_data['Indicator Name'] == criterion]
    WB_data= WB_data[column_name]
    #setting index    
    WB_data.set_index('Country Name', inplace = True)
    WB_data = WB_data.loc[country_name]
    #transpose the DataFrame
    WB_data_t = WB_data.transpose()  
    #Return two values, original data and transposed data
    return WB_data, WB_data_t

input_file = r"C:\Users\Lenovo\Desktop\see\WBDATA.xls"

country_name = ['Australia','United States','Brazil','Germany', 'Kenya','Canada']
column_name = ['Country Name', '1990','1996','2002','2008','2014','2020']
criterion = ['Mortality rate, under-5 (per 1,000 live births)','Population, total', 'Total greenhouse gas emissions (kt of CO2 equivalent)', 'Forest area (sq. km)', 'Electricity production from coal sources (% of total)']

#Data for both original and transposed mortality figure
mort, mort_r = file_read_transpose_csv(input_file,country_name,column_name,criterion[0])

#Data for both original and transposed total population figure
pop_total, pop_total_y = file_read_transpose_csv(input_file,country_name,column_name,criterion[1])

#Data for both original and transposed greenhouse gas emission figure
green_g, green_gy = file_read_transpose_csv(input_file,country_name,column_name,criterion[2])

#Data for both original and transposed forest area figure
Forest, Forest_y = file_read_transpose_csv(input_file,country_name,column_name,criterion[3])

#Data for both original and transposed electricity from coal figure
Elect, Elect_y = file_read_transpose_csv(input_file,country_name,column_name,criterion[4])


#plotting grouped bar chart to compare countries total greenhouse gas across time series
green_g.plot(kind='bar', rot = 45)
plt.title('Grouped Bar Chart Analysis of Greenhouse Gas Emission')
plt.xlabel('Countries')
plt.ylabel('Greenhouse Emission')
plt.rcParams.update({'figure.figsize':[8,6], 'lines.linewidth': 3, 'figure.dpi':200})
plt.show()
