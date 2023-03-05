# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:16:00 2023

@author: bhagy
"""

#Import required modules
import pandas as pd
import matplotlib.pyplot as plt

def loaddfxy(df, headers):
    """ Function to load data to Pandas dataframe with selected columns. 
        Arguments:
        A dataframe with a index "head" and other columns to be taken selected headers.
        A list containing the selected headers of the columns to create datadrame.
        For loop is used to fetch and assign data to dataframe(data_xy)
        After data is inserted into dataframe it will be return from the function.
    """
    #For loop to load required headers to DataFrame
    for head in headers:
        data_xy[head] = pd.DataFrame(data[head], columns=[head])
    
    return  # Function return the DataFrame data_xy

def loaddfjk(df, headers):
    """ Function to load data to Pandas dataframe with selected columns. 
        Arguments:
        A dataframe with a index "head" and other columns to be taken selected headers.
        A list containing the selected headers of the columns to create datadrame.
        For loop is used to fetch and assign data to dataframe(data_xy)
        After data is inserted into dataframe it will be return from the function.
    """
    #For loop to load required headers to DataFrame
    for head in headers:
        data_jk[head] = pd.DataFrame(data_air[head], columns=[head])
    
    return  # Function return the DataFrame data_xy
   
def lineplot_xy(df, headers):
    """ Function to create a lineplot. 
        Arguments:
        A dataframe with a column "Year" and other columns to be taken as headers.
        A list containing the headers of the columns to plot.
        For loop will be used to plot and matplotlib.pyplot used.
    """
    #Start to plot
    plt.figure()
    #For loop to load required data using headers.
    for head in headers:
        plt.plot(df[['Year']], df[head], label=head)
       
    #labelling x axis and y axis
    plt.xlabel('Year')
    plt.ylabel('Power Generation (GWh)')
    
    #Add legend to explain the each lineplot 
    plt.legend()
    #Add Title to the graph
    plt.title("UK Electricity generated Time Series")
    # save the plot output as png
    plt.savefig("linplot-UK Electricity generated Time Series.png")
    #Display the plot
    plt.show()

    return  #Function return the lineplot and save the image

def barplot_jk(df, headers):
    """ Function to create a barplot. 
        Arguments:
        A dataframe with a column "Year" and other columns to be taken as headers.
        A list containing the headers of the columns to plot.
        For loop will be used to plot and matplotlib.pyplot used.
    """
    #Start to plot
    plt.figure()
    
    plt.bar(df["year"], df["pm10"], label="pm10")
    plt.bar(df["year"], df["pm25"], label="pm25")

       
    #labelling x axis and y axis
    plt.xlabel('Year')
    plt.ylabel('Air Polution (AQI)')
    
    #Add legend to explain the each lineplot 
    plt.legend()
    #Add Title to the graph
    plt.title("Air Pollution in United Kingdom")
    # save the plot output as png
    plt.savefig("linplot-UK Air Pollution.png")
    #Display the plot
    plt.show()
    

    return  #Function return the lineplot and save the image

def pieplot(df, headers, RYear):
    """ Function to create a pieplot.
        Arguments:
        A signle dataframe with selected column and other columns to be taken as headers.
        The values are only containing for the selected headers of the columns to plot.
        Static passed data as argument will be used to plot the pie chart using matplotlib.pyplot.
    """
    #Start to plot
    plt.figure()
    
    plt.pie(df, labels=headers,  shadow = True, autopct='%1.1f%%')
    
    #Add Title to the graph
    plt.title("UK Electricty generating sources for the year {}".format(RYear))
    
    # save as png
    plt.savefig("pieplot-Electricty generating sources for the year {}.png".format(RYear))
    #Display the plot
    plt.show()

    return  #unction return the pieplot and save the image


#Start of main program
#Reading data from the source file. Here source file type is xlsx. 
#Therefore pandas reading funtion must be pd.read_excel
data = pd.read_excel("power_sources.xlsx")

#Define required headers to fetch data from required columns.  
headers = ["Conventional_thermal", "CCGT", "Nuclear", "Renewables", "Hydro"]

#Initialize pandas dataframe variable to load data. Here Year is used  for indexing.
data_xy = pd.DataFrame(data["Year"], columns=["Year"])

#Pass the data fetch from Convert data to pandas dataframe
loaddfxy(data, headers)


#Calling lineplot with a list of the columns to be plotted.
lineplot_xy(data_xy, headers)


#Calling pieplot to display Energy power source contribution for year 2021
RequestYear = data_xy.iloc[50, 0]
RequestData = data_xy.iloc[50, 1:6]
pieplot(RequestData, headers, RequestYear)


#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_air = pd.read_csv("air_pollution.csv")
print(data_air)

headersjk = ["nh3", "nox", "voc", "pm10", "pm25", "so2"]
print(headersjk)
#Convert data to pandas dataframe
data_jk = pd.DataFrame(data_air["year"], columns=["year"])
loaddfjk(data_air, headersjk)

print(data_jk["year"])
print(data_jk)


barplot_jk(data_jk, headersjk)












