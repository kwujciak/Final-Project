#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:42:57 2020

@author: katewujciak
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tourism = pd.read_csv("tourism_new.csv")
london = np.array(tourism)[:1]
years = [2014,2015,2016,2017,2018]
international = ["London","Rome","Tokyo"]

def graph_tourists(destination, future_yr):
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
    
    
#graph_London("New York", 2021)

#print(np.amin(tourism))
#print(np.amax(years))