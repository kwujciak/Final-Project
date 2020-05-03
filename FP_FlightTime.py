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
#print(ft[:1])
#print(ft[:,0])


#print(ft)
print(flight_time.iloc[5, 5])
print(flight_time.iloc[5, 6])
print(flight_time.iloc[5, 7])

def Main_flights(destination):
    origin = input("Are you flying from your current location? ")
    if origin == "yes" or "Yes":
        departure(destination)
    else:
        depart = input("Where will you be flying from? ")
            
def departure(destination):
    current_timezone = input("What is your current timezone (EDT, CDT, MDT, or PDT)? ")
    if current_timezone == "EDT":
        col = 7
    elif current_timezone == "CDT":
        col = 6
    elif current_timezone == "MDT":
        col = 5
    elif current_timezone == "PDT":
        col = 4
    if destination == "London":
        row = 1
    elif destination == "Rome":
        row = 2
    elif destination == "Tokyo":
        row = 3
    elif destination == "Los Angeles":
        row = 4
    elif destination == "Denver":
        row = 5
    elif destination == "Chicago":
        row = 6
    elif destination == "New York":
        row = 7
    print(flight_time.iloc[row, col])

Main_flights("Rome")

#def from_CDT(destination):
#    if destination == "London":
#        row = 1
#    elif destination == "Rome":
#        row = 2
#    elif destination == "Tokyo":
#        row = 3
#    elif destination == "Los Angeles":
#        row = 4
#    elif destination == "Denver":
#        row = 5
#    elif destination == "Chicago":
#        row = 6
#    elif destination == "New York":
#        row = 7
#    print(flight_time.iloc[row, 6])
#    
#def from_MDT(destination):
#    if destination == "London":
#        row = 1
#    elif destination == "Rome":
#        row = 2
#    elif destination == "Tokyo":
#        row = 3
#    elif destination == "Los Angeles":
#        row = 4
#    elif destination == "Denver":
#        row = 5
#    elif destination == "Chicago":
#        row = 6
#    elif destination == "New York":
#        row = 7
#    print(flight_time.iloc[row, 5])
#
#def from_PDT(destination):
#    if destination == "London":
#        row = 1
#    elif destination == "Rome":
#        row = 2
#    elif destination == "Tokyo":
#        row = 3
#    elif destination == "Los Angeles":
#        row = 4
#    elif destination == "Denver":
#        row = 5
#    elif destination == "Chicago":
#        row = 6
#    elif destination == "New York":
#        row = 7
#    print(flight_time.iloc[row, 4])
    
