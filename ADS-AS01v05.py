# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:16:00 2023

@author: bhagy
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def loaddf(df, headers):

    for head in headers:
        data_xy[head] = pd.DataFrame(data[head], columns=[head])
    
    return  # Functions should finish with return
   
def lineplot(df, headers):
    plt.figure()
    
    for head in headers:
        plt.plot(df[['Year']], df[head], label=head)
       
    print(df[['Year']])
    # labelling
    plt.xlabel('Year')
    plt.ylabel('Power Generation GWh')
    
    # removing white space left and right. Both standard and pandas min/max
    # can be used
    #plt.xlim(min(df["x"]), df["x"].max())

    plt.legend()
    # save as png
    plt.savefig("linplot.png")
    plt.show()

    return  # Functions should finish with return

def pieplot(df, headers):
    plt.figure()
    print(df)
    print(headers)
    plt.pie(df, labels=headers,  autopct='%1.1f%%')
       
    # labelling
   # plt.xlabel('Year')
   # plt.ylabel('Power Generation GWh')
    
    # removing white space left and right. Both standard and pandas min/max
    # can be used
    #plt.xlim(min(df["x"]), df["x"].max())

    #plt.legend()
    # save as png
    plt.savefig("pieplot.png")
    plt.title("PowerSource for year 2021")
    plt.show()

    return  # Functions should finish with return

#Reading data from the source file. Here source file type is xlsx. 
#Therefore pandas reading funtion must be pd.read_excel
data = pd.read_excel("power_sources.xlsx")
headers = ["conventional_thermal", "CCGT", "nuclear", "renewables", "hydro"]
#Convert data to pandas dataframe
data_xy = pd.DataFrame(data["Year"], columns=["Year"])
loaddf(data, headers)


# calling lineplot with a list of the columns to be plotted.
lineplot(data_xy, headers)


# calling pieplot to display Energy power source contribution for year 2021
pieplot(data_xy.iloc[51, 1:6], headers)







