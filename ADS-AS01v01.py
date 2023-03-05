# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:16:00 2023

@author: bhagy
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

"""
def lineplot(year, power_source, label, color ):
    Function to create a lineplot. 
        Arguments:
            Dataframe with a column "x" 
            Dataframe with a columns to be taken as y.
        A list containing the headers of the columns to plot.
    


    plt.figure()

    #
    for head in headers:
        plt.plot(df["x"], df[head], label=head)

    # labelling
    plt.xlabel('Year')
    plt.ylabel('Power Generation GWh')
    
    # removing white space left and right. Both standard and pandas min/max
    # can be used
    plt.xlim(min(df["x"]), df["x"].max())

    plt.legend()
    # save as png
    plt.savefig("linplot.png")
    plt.show()

    return  # Functions should finish with return


Reading data from the source file. Here source file type is xlsx. 
#Therefore pandas reading funtion must be pd.read_excel
"""
power_sources = pd.read_excel("power_sources.xlsx")

print(power_sources)


power_sources_index = power_sources.set_index('Year')


print(power_sources_index)




plt.plot(power_sources["Year"], power_sources["conventional_thermal"], label="Thermal", color='orange')
plt.plot(power_sources["Year"], power_sources["CCGT"], label="CCGT", color='brown')
plt.plot(power_sources["Year"], power_sources["nuclear"], label="Nuclear", color='red')
plt.plot(power_sources["Year"], power_sources["renewables"], label="Renewables", color='green')
plt.plot(power_sources["Year"], power_sources["hydro"], label="Hydro", color='blue')

plt.legend()
plt.xlabel('Year')
plt.ylabel('Power Generation (GWh)')

plt.show