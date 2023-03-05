# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 10:44:59 2023

@author: bhagy
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_air = pd.read_csv("air_pollution.csv")
print(data_air)

#Convert data to pandas dataframe
data_jk = pd.DataFrame(data_air["year"], columns=["year"])
data_jk["Ammonia"] = pd.DataFrame(data_air["nh3"], columns=["Ammonia"])
data_jk["nox"] = pd.DataFrame(data_air["nox"], columns=["nox"])
data_jk["voc"] = pd.DataFrame(data_air["voc"], columns=["voc"])
data_jk["pm10"] = pd.DataFrame(data_air["pm10"], columns=["pm10"])
data_jk["pm25"] = pd.DataFrame(data_air["pm25"], columns=["pm25"])
data_jk["so2"] = pd.DataFrame(data_air["so2"], columns=["so2"])

print(data_jk["year"])

plt.figure()
plt.bar(data_jk["year"], data_jk["Ammonia"], label="Ammonia")
plt.bar(data_jk["year"], data_jk["nox"], label="nox")
plt.bar(data_jk["year"], data_jk["voc"], label="voc")
plt.bar(data_jk["year"], data_jk["pm10"], label="pm10")
plt.bar(data_jk["year"], data_jk["pm25"], label="pm25")
plt.bar(data_jk["year"], data_jk["so2"], label="so2")
plt.title("Air Pollution in United Kingdom")
plt.xlabel("year")
plt.ylabel("AQI (Air Pollution Index)")
plt.legend()
plt.show()
