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


def Main_flights(destination):
    origin = input("Are you flying from your current location? ")
    if origin == "yes" or origin == "Yes":
        departure(destination)
    else:
        depart = input("Where will you be flying from? ")
        col = for_departure(depart)
        row = arrival(destination)
        print("The flight duration will be " + str(flight_time.iloc[row, col]))
            
            
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
        row = 0
    elif destination == "Rome":
        row = 1
    elif destination == "Tokyo":
        row = 2
    elif destination == "Los Angeles":
        row = 3
    elif destination == "Denver":
        row = 4
    elif destination == "Chicago":
        row = 5
    elif destination == "New York":
        row = 6
    print("The flight duration will be " + str(flight_time.iloc[row, col])+ ".")


def for_departure(depart):
    if depart == "London":
        col = 1
    elif depart == "Rome":
        col = 2
    elif depart == "Tokyo":
        col = 3
    elif depart == "Los Angeles":
        col = 4
    elif depart == "Denver":
        col = 5
    elif depart == "Chicago":
        col = 6
    elif depart == "New York":
        col = 7
    return col

def arrival(destination):
    if destination == "London":
        row = 0
    elif destination == "Rome":
        row = 1
    elif destination == "Tokyo":
        row = 2
    elif destination == "Los Angeles":
        row = 3
    elif destination == "Denver":
        row = 4
    elif destination == "Chicago":
        row = 5
    elif destination == "New York":
        row = 6
    return row

