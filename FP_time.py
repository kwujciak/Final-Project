#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:05:01 2020

@author: katewujciak
"""

import time
#print(time.localtime())

year = time.localtime()[0]
month = time.localtime()[1]
day = time.localtime()[2]
hour_military = time.localtime()[3]
minute = time.localtime()[4]
day = time.localtime()[5]
day_year = time.localtime()[6]

current_timezone = input("What is your current timezone (EDT, CDT, MDT, or PDT)? ")
destination = input("Where are you travelling (US, Japan, Europe)? ")


def Europe():
    if current_timezone == "EDT":
        new_hour = hour_military + 5
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))
    elif current_timezone == "CDT":
        new_hour = hour_military + 6
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))
    elif current_timezone == "MDT":
        new_hour = hour_military + 7
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute)) 
    elif current_timezone == "PDT":
        new_hour = hour_military + 8
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))
 
def Japan():
    if current_timezone == "EDT":
        new_hour = hour_military + 13
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))
    elif current_timezone == "CDT":
        new_hour = hour_military + 14
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))
    elif current_timezone == "MDT":
        new_hour = hour_military + 15
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute)) 
    elif current_timezone == "PDT":
        new_hour = hour_military + 16
        if new_hour >= 24:
            new_hour = new_hour - 24
            print(str(new_hour) + ":" + str(minute))
        else:
            print(str(new_hour) + ":" + str(minute))    
            
def US():
    US_timezone = input("What US time zone are you travelling to? ")
    if US_timezone == current_timezone:
        print(str(hour_military)+ ":" + str(minute))
    elif US_timezone == "EDT":
        if current_timezone == "CDT":
            new_hour = hour_military + 1
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "MDT":
            new_hour = hour_military + 2
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "PDT":
            new_hour = hour_military + 3
            print(str(new_hour) + ":" + str(minute))
    elif US_timezone == "CDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 1
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "MDT":
            new_hour = hour_military + 1
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "PDT":
            new_hour = hour_military + 2
            print(str(new_hour) + ":" + str(minute))
    elif US_timezone == "MDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 2
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "CDT":
            new_hour = hour_military - 1
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "PDT":
            new_hour = hour_military + 1
            print(str(new_hour) + ":" + str(minute))
    elif US_timezone == "PDT":
        if current_timezone == "EDT":
            new_hour = hour_military - 3
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "CDT":
            new_hour = hour_military - 2
            print(str(new_hour) + ":" + str(minute))
        elif current_timezone == "MDT":
            new_hour = hour_military - 1
            print(str(new_hour) + ":" + str(minute))
   

def time_zone():
    if destination == "Europe":
        Europe()
    elif destination == "Japan":
        Japan()
    elif destination == "US":
        US()
        
time_zone()
