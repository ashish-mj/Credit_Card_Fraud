#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:00:01 2021

@author: ashish
"""


import pandas as pd
import seaborn as sb
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = pd.read_csv("../creditcard.csv")
print(data.head())

'''
fraud_transactions = data.loc[data["Class"]==1]
print(len(fraud_transactions))
non_fraud_transactions = data.loc[data["Class"]==0]
print(len(non_fraud_transactions))

sb.relplot(x="Amount",y="Class",data=data)
sb.relplot(x="Amount",y="Time",hue="Class",data=data)
'''

x = data.iloc[:,:-1]
print(x.head())
y = data["Class"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

clf = linear_model.LogisticRegression(C=1e5)
clf.fit(x_train,y_train)