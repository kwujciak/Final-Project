#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:59:51 2020

@author: katewujciak
"""

import FP_time as time
import FP_currency as cur
import FP_attractions as at
import FP_FlightTime as ft

print("Welcome to your personal travel tool!")
print("Compatible destinations are:")
print("London, Rome, Tokyo, New York, Chicago, Denver, and Los Angeles")
destination = input("Where are you travelling?")

europe = ["London", "Rome"]
US = ["New York", "Chicago", "Denver", "Los Angeles"]
if destination in europe:
    time.Europe()
if destination == "Tokyo":
    time.Japan()
if destination in US:
    time.US()
