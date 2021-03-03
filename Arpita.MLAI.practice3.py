# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:30:55 2021

@author: cttc
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel(r"C:\Users\cttc\Desktop\Datasets\Hourly temperature data.xlsx")
data.dtypes
data.isnull().sum()

data.columns = ['Row_Labels','Day','Count_of_Gross']

des = data.describe(include = 'all' )


data.Row_Labels = data.Row_Labels.astype('str')


'''

str(data.Row_Labels[0]).split()[0]


for i in range(0, 90):
    data.Row_Labels.replace(data.Row_Labels[i], str(data.Row_Labels[i]).split()[i], inplace = True)


data.Row_Labels.replace(data.Row_Labels[0], str(data.Row_Labels[0]).split()[0])


def f_(s):
    s = str(s)
    return s.split()[0]

res =  map(f_, data.Row_Labels)
res1 = list(map(f_, data.Row_Labels)).copy()

len(list(res1))
print(list(res1))

for i in range(0,90):
    data.Row_Labels.replace(data.Row_Labels[i], list(map(f_, data.Row_Labels))[i],
                            inplace = True)
'''





from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
ip = data.drop(["Count_of_Gross"],axis=1)
op = data["Count_of_Gross"]
xtr,xts,ytr,yts = train_test_split(ip,op,test_size=0.2,random_state=0)

alg = LogisticRegression()
alg.fit(xtr,ytr)




