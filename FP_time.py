#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:05:01 2020

@author: katewujciak
"""

import time

hour_military = time.localtime()[3]
minute = time.localtime()[4]
europe = ["London", "Rome"]
USA = ["New York", "Chicago", "Denver", "Los Angeles"]

def Main_time(destination):
    current_timezone = input("What is your current timezone (EDT, CDT, MDT, or PDT)? ")
    if destination in europe:
        new_h = Europe(current_timezone)
        print("The time in " + str(destination) + " is " + str(new_h) + ":" + str(minute))
    elif destination == "Tokyo":
        new_h = Japan(current_timezone)
        print("The time in Tokyo is " + str(new_h) + ":" + str(minute))
    elif destination in USA:
        new_h = US(current_timezone, destination)
        print("The time in " + str(destination) + " is " + str(new_h) + ":" + str(minute))
    
def Europe(current_timezone):
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
    US_timezone = US_time(destination)
    if US_timezone == current_timezone:
        new_hour = hour_military
        return new_hour
#        print(str(hour_military)+ ":" + str(minute))
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

 
   

#def time_zone(destination):
#    if destination == "Rome" or destination == "London":
#        Europe()
#    elif destination == "Japan":
#        Japan()
#    elif destination == "US":
#        US()
#        
#time_zone(destination)
