#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:22:03 2020

@author: katewujciak
"""


def Main_currency(destination):
    if destination == "Tokyo":
        answer = input("Would you like to convert to from USD to Yen? ")
        if answer == "yes" or answer == "Yes":
            amount = float(input("How much would you like to convert (enter number)? "))
            US_Yen(amount, "US to Yen")
        else:
            backup(amount)
    elif destination == "London":
        answer = input("Would you like to convert to from USD to Pound? ")
        amount = float(input("How much would you like to convert (enter number)? "))
        if answer == "yes" or answer == "Yes":
            US_Pound(amount, "US to Pound")
        else:
            backup(amount) 
    elif destination == "Rome":
        answer = input("Would you like to convert to from USD to Euro? ")
        amount = float(input("How much would you like to convert (enter number)? "))
        if answer == "yes" or answer == "Yes":
            US_Euro(amount, "US to Euro")
        else:
            backup(amount)   
    else:
        print("You do not need to convert.")

def US_Pound(amount, convert):
    if convert == "US to Pound":
        pound = round((0.81*amount),2)
        print("£" + str(pound))
    elif convert == "Pound to US":
        dollar = round((1.24*amount),2)
        print("$" + str(dollar))

def US_Yen(amount, convert):
    if convert == "US to Yen":
        yen = round((107.47*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to US":
        dollar = round((0.0093*amount),2)
        print("$" + str(dollar))

def US_Euro(amount, convert):
    if convert == "US to Euro":
        euro = round((0.92*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to US":
        dollar = round((1.08*amount),2)
        print("$" + str(dollar))

def Pound_Euro(amount, convert):
    if convert == "Pound to Euro":
        euro = round((1.14*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to Pound":
        pound = round((0.87*amount),2)
        print("£" + str(pound))

def Pound_Yen(amount, convert):
    if convert == "Pound to Yen":
        yen = round((132.89*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Pound":
        pound = round((0.0075*amount),2)
        print("£" + str(pound))
    
def Euro_Yen(amount, convert):
    if convert == "Euro to Yen":
        yen = round((116.31*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Euro":
        euro = round((0.0086*amount),2)
        print("€" + str(euro))

def backup(amount):
    convert = input("What would you like to convert? ")    
    if "Pound" and "Euro" in convert:
        Pound_Euro(amount, convert)
    elif "US" and "Pound" in convert:
        US_Pound(amount, convert)
    elif "US" and "Yen" in convert:
        US_Yen(amount, convert)
    elif "US" and "Euro" in convert:
        US_Euro(amount, convert)
    elif "Pound" and "Yen" in convert:
        Pound_Yen(amount, convert)
    elif "Yen" and "Euro" in convert:
        Euro_Yen(amount, convert)
    else:
        print("cannot convert")
    
    
    
#if "Pound" and "Euro" in convert:
#    Pound_Euro(amount)

#else:
#    print(" ")
#    
#if convert == "US to Euro" or convert == "Euro to US":
#    US_Euro(amount)
#elif convert == "Yen to Pound" or convert == "Pound to Yen":
#    Pound_Yen(amount)
#elif convert == "Yen to Euro" or convert == "Euro to Yen":
#    Euro_Yen(amount)
#else:
#    print("Cannot convert this currency")