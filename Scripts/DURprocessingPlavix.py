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
file = 'https://github.com/StatsGuru/Glucksman/blob/master/NationalDUR2011-2013.txt'
df = pd.read_csv(file, sep='|')
print(df.head())

#input NDC list for Plavix
file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/PlavixNDCs.csv'
NDClist = pd.read_csv(file)

#%%
"""
Processing the data
"""

#appends a record in the dataframe if it matches a certain productCode and laberCode
def productCodeFilter(productCode, labelCode, df):
    dfshort = df[(df["ProductCode"] == productCode) & (df["LabelerCode"] == labelCode)]
    return dfshort

dfshort = productCodeFilter(410, 51079, df)
print(dfshort.head())


def multiproductexporter(NDClist, df):
    dflong = pd.DataFrame(columns = list(df.columns.values))
    for i in range(len(NDClist)):
        dflong = dflong.append(productCodeFilter(NDClist['ProductCode'][i], NDClist['LabelerCode'][i], df))
    return dflong

#establish dataframe, process data, and export to csv    
dfproduct = pd.DataFrame(columns = list(df.columns.values))    
dfproduct = dfproduct.append(multiproductexporter(NDClist, df))
dfproduct.to_csv('Plavix2011-2013.csv')


