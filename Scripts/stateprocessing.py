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
import zipfile as zf
import io
import requests

#%%
"""
Inputing the data
"""

#extract file into statehealthdata folder
file = 'http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip'
response = requests.get(file)
zipDocument = zipfile.ZipFile(io.BytesIO(response.content))
zipDocument.extractall()
df

df = pd.read_csv(file,http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip sep='|')
print(df.head())

#input NDC list for Plavix
file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/master/ZyprexaNDCs.csv'
NDClist = pd.read_csv(file)

#%%df
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
dfproduct.to_csv('Zyprexa2011-2013.csv')


