#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:22:03 2020

@author: katewujciak
"""

convert = input("What would you like to convert? ")
amount = float(input("How much would you like to convert (enter number)? "))

def US_pound(amount):
    if convert == "US to Pound":
        pound = round((0.81*amount),2)
        print("£" + str(pound))
    elif convert == "Pound to US":
        dollar = round((1.24*amount),2)
        print("$" + str(dollar))

def US_Yen(amount):
    if convert == "US to Yen":
        yen = round((107.47*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to US":
        dollar = round((0.0093*amount),2)
        print("$" + str(dollar))

def US_Euro(amount):
    if convert == "US to Euro":
        euro = round((0.92*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to US":
        dollar = round((1.08*amount),2)
        print("$" + str(dollar))

def Pound_Euro(amount):
    if convert == "Pound to Euro":
        euro = round((1.14*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to Pound":
        pound = round((0.87*amount),2)
        print("£" + str(pound))

def Pound_Yen(amount):
    if convert == "Pound to Yen":
        yen = round((132.89*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Pound":
        pound = round((0.0075*amount),2)
        print("£" + str(pound))
    
def Euro_Yen(amount):
    if convert == "Euro to Yen":
        yen = round((116.31*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Euro":
        euro = round((0.0086*amount),2)
        print("€" + str(euro))

if "Pound" and "Euro" in convert:
    Pound_Euro(amount)
elif "US" and "Pound" in convert:
    US_pound(amount)
elif "US" and "Yen" in convert:
    US_Yen(amount)
else:
    print(" ")
    
if convert == "US to Euro" or convert == "Euro to US":
    US_Euro(amount)
elif convert == "Yen to Pound" or convert == "Pound to Yen":
    Pound_Yen(amount)
elif convert == "Yen to Euro" or convert == "Euro to Yen":
    Euro_Yen(amount)
else:
    print("Cannot convert this currency")