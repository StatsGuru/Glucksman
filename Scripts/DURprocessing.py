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

file = 'https://raw.githubusercontent.com/StatsGuru/Glucksman/9a995d7f93f36a5fcde83ede8a660478a3711f71/NationalDUR2013.TXT'
df = pd.read_csv(file, sep='|')
print(df.head())