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

file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/NationalDUR2013.TXT'
df = pd.read_csv(file, sep='|')
print(df.head())


#%%

file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/LipitorNDCs.csv'
NDClist = pd.read_csv(file)

dfproduct = pd.DataFrame(columns = list(df.columns.values))
#%%
def productcodeexporter(productCode, labelerCode, df):
    dfshort = pd.DataFrame(columns = list(df.columns.values))
    for i in df.index:
        if (df["ProductCode"][i] == productCode and df["LabelerCode"][i] == labelerCode):
            rowtoappend = df[i:i+1]
            dfshort = dfshort.append(rowtoappend)
    return dfshort

def multiproductexporter(rxlist, labellist, df):
    dflong = pd.DataFrame(columns = list(df.columns.values))
    for i in range(len(rxlist)):
        dflong = dflong.append(productcodeexporter(rxlist[i], labellist[i], df))
    return dflong
    
dfproduct = dfproduct.append(multiproductexporter(NDClist['ProductCode'], NDClist['LabelerCode'], df))
dfproduct.to_csv('changethenameofthisfile2013.csv')


