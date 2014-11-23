# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 20:02:01 2014

@author: EasyLoverJeremy
"""

#%%
"""
Import the necessary libraries to do the statistical analysis
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

#%%
"""
Inputing the data
"""

#Input national DUR file
file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/NationalDUR2013.TXT'
df = pd.read_csv(file, sep='|')
print(df.head())

#input NDC list for Lipitor
file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/LipitorNDCs.csv'
NDClist = pd.read_csv(file)

#%%
"""
Processing the data
"""

#appends a record in the dataframe if it matches a certain productCode and laberCode
def productCodeFilter(productCode, labelCode, df):
    dfshort = df[(df["ProductCode"] == productCode and df["LabelerCode"] == labelCode)]
    return dfshort

dfshort = productCodeFilter(410, 20, df)
#%%

#iterates through a list doing, productcodeexporter for each item in a list
def multiproductexporter(rxlist, labellist, df):
    dflong = pd.DataFrame(columns = list(df.columns.values))
    for i in range(len(rxlist)):
        dflong = dflong.append(productCodeFilter(rxlist[i], labellist[i], df))
    return dflong

#establish dataframe, process data, and export to csv    
dfproduct = pd.DataFrame(columns = list(df.columns.values))    
dfproduct = dfproduct.append(multiproductexporter(NDClist['ProductCode'], NDClist['LabelerCode'], df))
dfproduct.to_csv('changethenameofthisfile2013.csv')


