#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kate Wujciak
Worked alone
FP_FlightTime.py
Flight time duration calculator.
"""

import pandas as pd
import numpy as np


flight_time = pd.read_csv("flight_times.csv")
ft = np.array(flight_time)


def Main_flights(destination):
# Parameters: 
    # destination: the desired destination based on user input. 
#Function purpose:
    # This is the main flight duration function. Based on user input, it will
    # determine the origin location.
#Return value:
    # Void
    origin = input("Are you flying from your current location? ")
    if origin == "yes" or origin == "Yes":
        departure(destination)
    else:
        depart = input("Where will you be flying from? ")
        col = for_departure(depart)
        row = arrival(destination)
        print("The flight duration will be " + str(flight_time.iloc[row, col]))
            
            
def departure(destination):
# Parameters: 
    # destination: the desired destination based on user input. 
#Function purpose:
    # This function finds the flight duration if the user is leaving from their
    # current location.
#Return value:
    # Void
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
# Parameters: 
    # depart: the desired departing location based on user input. 
#Function purpose:
    # Assigns appropriate column based on location.
#Return value:
    # col: column of departing location.
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
# Parameters: 
    # destination: the desired departing location based on user input. 
#Function purpose:
    # Assigns appropriate row based on destination.
#Return value:
    # row: row of destination.
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

