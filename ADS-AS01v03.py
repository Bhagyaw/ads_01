# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:16:00 2023

@author: bhagy
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


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


#Reading data from the source file. Here source file type is xlsx. 
#Therefore pandas reading funtion must be pd.read_excel
data = pd.read_excel("power_sources.xlsx")

#Convert data to pandas dataframe
data_xy = pd.DataFrame(data["Year"], columns=["Year"])
data_xy["conventional_thermal"] = pd.DataFrame(data["conventional_thermal"], columns=["conventional_thermal"])
data_xy["CCGT"] = pd.DataFrame(data["CCGT"], columns=["CCGT"])
data_xy["nuclear"] = pd.DataFrame(data["nuclear"], columns=["nuclear"])
data_xy["renewables"] = pd.DataFrame(data["renewables"], columns=["renewables"])
data_xy["hydro"] = pd.DataFrame(data["hydro"], columns=["hydro"])

# calling lineplot with a list of the columns to be plotted.
lineplot(data_xy, ["conventional_thermal", "CCGT", "nuclear", "renewables", "hydro"])


#Energy power source contribution for year 2021
energyvalue = data_xy.iloc[51, 1:6]
print(energyvalue)
energysource = ["conventional_thermal", "CCGT", "nuclear", "renewables", "hydro"]
plt.figure()
plt.pie(energyvalue, labels=energysource,  autopct='%1.1f%%')
plt.title("PowerSource for year 2021")
plt.show()





