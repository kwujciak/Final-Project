#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:48:45 2020

@author: katewujciak
"""

import numpy as np
import pandas as pd

attractions = pd.read_csv("attractions.csv")
att = np.array(attractions)
locations = att[:,0]
att_list = att[:,1]
#print(locations)


def attract(destination):
    return attractions["Popular Attraction"][attractions["Unnamed: 0"].str.match(destination)]

popular = attract(destination)
print("A attraction you may want to visit: " + str(popular))
