# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 20:02:01 2014

@author: EasyLoverJeremy
"""

#%%
"""
Import the necessary libraries to do the statistical analysis
"""

import zipfile, urllib, csv
def get_items('http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip'):
  zip, headers = urllihttp://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zipb.urlretrieve('http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip')
  with zipipfile.ZipFile(zip) as http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zipzf:
    csvfiles = [name for name in zf.namelist()
                 if name.endswith('.csv')]
    for filename in csvfiles:
      with zf.open(filename) as source:
        reader = csv.DictReader([line.decode('iso-8859-1')
                                  for line in source])
        for item in reader:
          yield item
  os.unlink(zip)

#%%
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

#%%
"""
Inputing the data
"""
http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip
#Input national DUR filehthttp://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.ziptp://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Preschttp://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zipription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zip
file = 'http://www.medicaid.gov/Medicaid-CHIP-Program-Information/By-Topics/Benefits/Prescription-Drugs/Downloads/Rx-By-State/AK/AKUTIL13.zips/Downloads/Rx-By-State/AK/AKUTIL13.zip'
df = pd.read_csv(file, sep='|')
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


