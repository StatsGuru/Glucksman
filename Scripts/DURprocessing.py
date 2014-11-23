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

file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/2b600409d92339530eef30e7d42995a984625550/NationalDUR2013.TXT'
df = pd.read_csv(file, sep='|')
print(df.head())

#%%

df2 = list(df.columns.values)
print(df2)
rowtoappend = df[1:2]
df3=pd.DataFrame(columns = df2)
df3.append(rowtoappend)
#%%

df3=pd.DataFrame(columns = df2)
df3.append(df[1])
print(df3)

df["ProductCode"]
#%%
dfproduct = pd.DataFrame(columns = list(df.columns.values))

def productcodeexporter(code, df):
    dfshort = pd.DataFrame(columns = list(df.columns.values))
    for i in df.index:
        if df["ProductCode"][i] == code:
            rowtoappend = df[i:i+1]
            dfshort = dfshort.append(rowtoappend)
    return dfshort

def multiproductexporter(rxlist, df):
    dflong = pd.DataFrame(columns = list(df.columns.values))
    for i in range(len(rxlist)):
        dflong = dflong.append(productcodeexporter(rxlist[i], df))
    return dflong
    
dfproduct = dfproduct.append(multiproductexporter([5810,5820], df))