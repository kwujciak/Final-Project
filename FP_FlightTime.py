#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:39:03 2020

@author: katewujciak
"""

import pandas as pd
import numpy as np

flight_time = pd.read_csv("flight_times.csv")
ft = np.array(flight_time)
print(ft[:1])
print(ft[:,0])