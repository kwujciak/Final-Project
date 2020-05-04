#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kate Wujciak
Worked alone
FP_time.py
Displays the time in desired destination.
"""

import time

hour_military = time.localtime()[3]
minute = time.localtime()[4]
europe = ["London", "Rome"]
USA = ["New York", "Chicago", "Denver", "Los Angeles"]

def Main_time(destination):
# Parameters: 
    # destination: the desired destination based on user input. 
#Function purpose:
    # This is the main time zone function. Based on the current timezone and 
    # destination, it calls the appropriate function and prints the new time.
#Return value:
    # current_timezone: current time of user.
    current_timezone = input("What is your current timezone (EDT, CDT, MDT, or PDT)? ")
    if destination in europe:
        new_h = Europe(current_timezone)
        print("The time in " + str(destination) + " is " + str(new_h) + ":" + str(minute))
        return current_timezone
    elif destination == "Tokyo":
        new_h = Japan(current_timezone)
        print("The time in Tokyo is " + str(new_h) + ":" + str(minute))
        return current_timezone
    elif destination in USA:
        new_h = US(current_timezone, destination)
        print("The time in " + str(destination) + " is " + str(new_h) + ":" + str(minute))
        return current_timezone
    
def Europe(current_timezone):
# Parameters: 
    # current_timezone: current time of user. 
#Function purpose:
    # This function takes the user's current timezone and calculates the current
    # time in Europe. 
#Return value:
    # new_hour: time at destination.
    if current_timezone == "EDT":
        new_hour = hour_military + 5
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "CDT":
        new_hour = hour_military + 6
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "MDT":
        new_hour = hour_military + 7
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "PDT":
        new_hour = hour_military + 8
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
 
def Japan(current_timezone):
# Parameters: 
    # current_timezone: current time of user. 
#Function purpose:
    # This function takes the user's current timezone and calculates the current
    # time in Japan. 
#Return value:
    # new_hour: time at destination.
    if current_timezone == "EDT":
        new_hour = hour_military + 13
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "CDT":
        new_hour = hour_military + 14
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "MDT":
        new_hour = hour_military + 15
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
    elif current_timezone == "PDT":
        new_hour = hour_military + 16
        if new_hour >= 24:
            new_hour = new_hour - 24
            return new_hour
        else:
            return new_hour
            
def US(current_timezone, destination):
# Parameters: 
    # current_timezone: current time of user. 
    # destination: the desired destination based on user input.
#Function purpose:
    # This function takes the user's current timezone and calculates the current
    # time at the destination. 
#Return value:
    # new_hour: time at destination.
    US_timezone = US_time(destination)
    if US_timezone == current_timezone:
        new_hour = hour_military
        return new_hour
    elif US_timezone == "EDT":
        if current_timezone == "CDT":
            new_hour = hour_military + 1
            return new_hour
        elif current_timezone == "MDT":
            new_hour = hour_military + 2
            return new_hour
        elif current_timezone == "PDT":
            new_hour = hour_military + 3
            return new_hour
    elif US_timezone == "CDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 1
            return new_hour
        elif current_timezone == "MDT":
            new_hour = hour_military + 1
            return new_hour
        elif current_timezone == "PDT":
            new_hour = hour_military + 2
            return new_hour
    elif US_timezone == "MDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 2
            return new_hour
        elif current_timezone == "CDT":
            new_hour = hour_military - 1
            return new_hour
        elif current_timezone == "PDT":
            new_hour = hour_military + 1
            return new_hour
    elif US_timezone == "PDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 3
            return new_hour
        elif current_timezone == "CDT":
            new_hour = hour_military - 2
            return new_hour
        elif current_timezone == "MDT":
            new_hour = hour_military - 1
            return new_hour

def US_time(destination):
# Parameters: 
    # destination: the desired destination based on user input.
#Function purpose:
    # This function takes the user's inputed destination (if in the US)
    # and finds its corresponding timezone.
#Return value:
    # US_timezone: timezone of destination.
    if destination == "New York":
        US_timezone = "EDT"
        return US_timezone
    elif destination == "Chicago":
        US_timezone = "CDT"
        return US_timezone
    elif destination == "Denver":
        US_timezone = "MDT"
        return US_timezone
    elif destination == "Los Angeles":
        US_timezone = "PDT"
        return US_timezone 

