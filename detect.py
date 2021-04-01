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