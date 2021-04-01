#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:00:01 2021

@author: ashish
"""

import numpy as np
import pandas as pd
import seaborn as sb

data = pd.read_csv("../creditcard.csv")
print(data.head())

fraud_transactions = data.loc[data["Class"]==1]
print(len(fraud_transactions))
non_fraud_transactions = data.loc[data["Class"]==0]
print(len(non_fraud_transactions))

sb.relplot(x="Amount",y="Class",data=data)