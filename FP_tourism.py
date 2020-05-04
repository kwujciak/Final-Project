#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kate Wujciak
Worked alone
FP_tourism.py
This file graphs the statistics on tourists per year in each destination.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tourism = pd.read_csv("tourism_new.csv")
london = np.array(tourism)[:1]
years = [2014,2015,2016,2017,2018]
international = ["London","Rome","Tokyo"]

def graph_tourists(destination, future_yr):
# Parameters: 
    # destination: the desired destination based on user input. 
    # future_yr: user-inputted year.
#Function purpose:
    # Graphs the annual number of tourists to a given location. It also
    # graphs the line of best fit and predicts number of tourists
    # for the given year.
#Return value:
    # Void
    if destination == "London":
        start = 0
        stop = 1
        mid = 2016
        med = 18.6
    if destination == "Rome":
        start = 1
        stop = 2
        mid = 2016
        med = 12
    if destination == "Tokyo":
        start = 2
        stop = 3  
        mid = 2018
        med = 14.2
    if destination == "Los Angeles":
        start = 3
        stop = 4
        mid = 2015
        med = 45.6
    if destination == "Denver":
        start = 4
        stop = 5
        mid = 2018
        med = 17.3
    if destination == "Chicago":
        start = 5
        stop = 6
        mid = 2017
        med = 55
    if destination == "New York":
        start = 6
        stop = 7
        mid = 2018
        med = 65.2
        
    y_val = np.array(tourism)[start:stop]
    x = np.array(years)
    m = (np.amax(y_val)-np.amin(y_val))/(np.amax(years)-np.amin(years))
    y = (m*(x-mid))+med
    plt.plot(x,y)
    
    if destination in international:
        plt.title("Interrnational Tourists in "+ str(destination))
    else:
        plt.title("Total Tourists in "+ str(destination))
    plt.scatter(x, y_val, alpha=0.5)
    plt.xlabel("Year")
    plt.ylabel("Tourists (in millions)")
    plt.xticks(np.arange(2013, 2020, 1))
    plt.yticks(np.arange(np.amin(y_val), np.amax(y_val), 1))
    plt.show()
    
    y1 = (m*(future_yr-mid))+med
    print("The predicted # of tourists in " + str(destination) + " in " + str(future_yr) + " is " + str(int(y1)) + " million.")
    if future_yr == 2020:
        print("This number may be affected by the COVID-19 crisis.") 
#print(np.amin(tourism))
#print(np.amax(years))