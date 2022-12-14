#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing python libraries to carry out data importation, sorting, analysis and presentation

"""
Created on Sat Dec 10 23:19:11 2022

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import describe

# setting display to show rows and column for easy readability

pd.set_option('max_rows', 63)
pd.set_option('max_columns', 10)


# Creation of function to read and transpose data

def file_read_transpose_csv(
    input_file,
    country_name,
    column_name,
    criterion,
    ):
    """read and transposes a csv file, returning both the original file and the transpose file,
    with header provided for transpose file.
    skiprows: used to remove first three line rows within the DataFrame
    input_file: file to be read    
    Country_name :column bearing 'Country name'
    column_name = list of columns within the dataframe
    Criterion : list of indicators to work with
    WB_data: name of the dataframe
     """

    WB_data = pd.read_excel(input_file, skiprows=3)

    # Subset the dataframe to only include rows of selected variables of selected columns

    WB_data = WB_data[WB_data['Indicator Name'] == criterion]
    WB_data = WB_data[column_name]

    # setting index

    WB_data.set_index('Country Name', inplace=True)
    WB_data = WB_data.loc[country_name]

    # transpose the DataFrame

    WB_data_t = WB_data.transpose()

    # Return two values, original data and transposed data

    return (WB_data, WB_data_t)


# Reading file

input_file = r"C:\Users\Lenovo\Desktop\see\WBDATA.xls"

country_name = [
    'Australia',
    'United States',
    'Brazil',
    'Germany',
    'Kenya',
    'Canada',
    ]
column_name = [
    'Country Name',
    '1990',
    '1996',
    '2002',
    '2008',
    '2014',
    '2020',
    ]
criterion = ['Mortality rate, under-5 (per 1,000 live births)',
             'Population, total',
             'Total greenhouse gas emissions (kt of CO2 equivalent)',
             'Forest area (sq. km)',
             'Electricity production from coal sources (% of total)']

# Data for both original and transposed mortality figure

(mort, mort_r) = file_read_transpose_csv(input_file, country_name,
        column_name, criterion[0])

# Data for both original and transposed total population figure

(pop_total, pop_total_y) = file_read_transpose_csv(input_file,
        country_name, column_name, criterion[1])

# Data for both original and transposed greenhouse gas emission figure

(green_g, green_gy) = file_read_transpose_csv(input_file, country_name,
        column_name, criterion[2])

# Data for both original and transposed forest area figure

(Forest, Forest_y) = file_read_transpose_csv(input_file, country_name,
        column_name, criterion[3])

# Data for both original and transposed electricity from coal figure

(Elect, Elect_y) = file_read_transpose_csv(input_file, country_name,
        column_name, criterion[4])

# Calculating statistical summary for population: Pop_stats

Pop_stats = describe(pop_total_y)
for key,value in Pop_stats._asdict().items():
    print(pop_total_y, f"{key}: {value}")

# plotting grouped bar chart to compare countries total greenhouse gas across time series

green_g.plot(kind='bar', rot=45)
plt.title('Grouped Bar Chart Analysis of Greenhouse Gas Emission'.upper(),
          fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Greenhouse Emission', fontweight='bold')
plt.rcParams.update({'figure.figsize': [8, 6], 'lines.linewidth': 3,
                    'figure.dpi': 200})

# Save and show plot

plt.savefig('Group_bar_Greenhouse_gas.png')
plt.show()

# plotting grouped bar chart to compare population of various countries across time series

pop_total.plot(kind='bar', rot=45)
plt.title('Grouped Bar Chart of Population Distribution'.upper(),
          fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.rcParams.update({'figure.figsize': [8, 6], 'lines.linewidth': 3,
                    'figure.dpi': 200})

# Save and show plot

plt.savefig('Group_bar_Population.png')
plt.show()


# Producing a line plot from for Forest Data

def line_plot(
    Forest_y,
    title,
    x_label,
    y_label,
    ):
    '''Plots a line graph of forest area across time series
    Forest_y: Forest data    
    Title :title of chart
    x_label : x-axis label
    y_label: y_axis label'''

    plt.figure(figsize=(10, 5))
    Forest_y.plot(legend=True, kind='line', style='--')
    plt.title(title.upper(), fontweight='bold')
    plt.legend(bbox_to_anchor=(1, 1))
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')

    # save and show plot

    plt.savefig('Line_plot_forest.png')
    return plt.show()


title1 = 'Forest Distribution Chart'
x_label1 = 'Year'
y_label1 = 'Country'

line_plot(Forest_y, title1, x_label1, y_label1)


# Plotting Line graph from Electricty generted from coal data

def line_plot(
    Elect_y,
    title,
    x_label,
    y_label,
    ):
    '''Plots a line graph of electricity generation from coal across time series
    Elect_y: Electricity data    
    Title :title of chart
    x_label : x-axis label
    y_label: y_axis label'''

    plt.figure(figsize=(10, 5))
    Elect_y.plot(legend=True, kind='line', style='--')
    plt.title(title.upper(), fontweight='bold')
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')

    # Save and show plot

    plt.savefig('Line_plot_Electricity.png')
    return plt.show()


title1 = 'Electricity generation from coal'
x_label1 = 'Year'
y_label1 = 'Country'

line_plot(Elect_y, title1, x_label1, y_label1)

# ------------------------------------------------------------------------------
# Creating DataFrame for United States with indicators

United_States = pd.DataFrame({
    'Population': pop_total_y['United States'],
    'Greenhouse gas': green_gy['United States'],
    'Mortality': mort_r['United States'],
    'Forest area': Forest_y['United States'],
    'Electricity ': Elect_y['United States'],
    }, [
    '1990',
    '1996',
    '2002',
    '2008',
    '2014',
    '2020',
    ])

# cleaning Dataframe by coverting NaNs to zeros

United_States = United_States.fillna(0)

# calcualting correlation for United States

United_States.corr()

# Plotting Heatmap correlation for United State

US_cor = United_States.corr()
plt.imshow(US_cor, cmap='summer', interpolation='none')
plt.colorbar()
plt.xticks(range(len(United_States.columns)), United_States.columns,
           rotation=65)
plt.yticks(range(len(United_States.columns)), United_States.columns)
plt.gcf().set_size_inches(8, 8)

lab = US_cor.values
for a in range(lab.shape[0]):
    for b in range(lab.shape[1]):
        plt.text(
            b,
            a,
            '{:.2f}'.format(lab[a, b]),
            ha='center',
            va='center',
            color='black',
            )
plt.title('United States Correlation Heatmap'.upper(), fontweight='bold'
          )

# Save and Show plot

plt.savefig('US_Heatmap.png')
plt.show()

# ------------------------------------------------------------------------------
# Creating DataFrame for Germany with indicators

Germany = pd.DataFrame({
    'Population': pop_total_y['Germany'],
    'Greenhouse gas': green_gy['Germany'],
    'Mortality': mort_r['Germany'],
    'Forest area': Forest_y['Germany'],
    'Electricity ': Elect_y['Germany'],
    }, [
    '1990',
    '1996',
    '2002',
    '2008',
    '2014',
    '2020',
    ])

# Cleaning DataFrame by coverting NaNs to zeros

Germany = Germany.fillna(0)

# Calculating Correlation for Germany

Germany.corr()

# Plotting Heatmap Correlation for Germany

germ_cor = Germany.corr()
plt.imshow(germ_cor, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(Germany.columns)), Germany.columns, rotation=65)
plt.yticks(range(len(Germany.columns)), Germany.columns)
plt.gcf().set_size_inches(8, 8)

lab = germ_cor.values
for a in range(lab.shape[0]):
    for b in range(lab.shape[1]):
        plt.text(
            b,
            a,
            '{:.2f}'.format(lab[a, b]),
            ha='center',
            va='center',
            color='black',
            )
plt.title('Germany Correlation Heatmap'.upper(), fontweight='bold')
plt.savefig('Germany_Heatmap.png')
