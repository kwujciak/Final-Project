#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kate Wujciak
Worked alone
FP_attractions.py
Displays popular attractions for each destinations.
"""

import numpy as np
import pandas as pd

attractions = pd.read_csv("attractions.csv")
att = np.array(attractions)
locations = att[:,0]
att_list = att[:,1]

def attract(destination):
# Parameters: 
    # destination: the desired destination based on user input. 
#Function purpose:
    # Finds popular attraction sites at each destination.
#Return value:
    # Void function.
    popular = attractions["Popular Attraction"][attractions["Unnamed: 0"].str.match(destination)]
    print("A attraction you may want to visit: " + str(popular))
