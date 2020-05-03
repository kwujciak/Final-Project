#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:59:51 2020

@author: katewujciak
"""
import FP_time as time_fnc
import FP_currency as cur
import FP_attractions as at
import FP_FlightTime as ft
import FP_tourism as tour


print("Welcome to your personal travel tool!")
print("Compatible destinations are:")
print("London, Rome, Tokyo, New York, Chicago, Denver, and Los Angeles")
tools = input("What would you like to know about your destination? ")
options = list(tools.split(" ")) 
time_words = ["time", "Time", "timezone", "Timezone"]
curr_words = ["currency", "Currency", "exchange", "Exchange", "money"]
attract_words = ["attraction", "attractions", "Attraction", "popular", "place", "places", "location"]
flight_words = ["flight", "duration", "Flight", "Duration", "airtime", "plane", "Plane"]
tourist_words = ["tourist", "Tourist", "statistics", "stats", "year", "tourism"]
destination = input("Where are you travelling? ")

if any(x in options for x in time_words):
    time_fnc.Main_time(destination)
if any(x in options for x in curr_words):
    cur.Main_currency(destination)
if any(x in options for x in attract_words):
    at.attract(destination)
if any(x in options for x in flight_words):
    ft.Main_flights(destination)
if any(x in options for x in tourist_words):
    future_yr = int(input("Please input a future year for the # of predicted tourists. "))
    tour.graph_tourists(destination, future_yr)
    








