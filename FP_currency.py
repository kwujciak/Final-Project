#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kate Wujciak
Worked alone
FP_currency.py
Currency converter file.
"""

def Main_currency(destination):
# Parameters: 
    # destination: the desired destination based on user input. 
#Function purpose:
    # This is the main currency exchange function. Based on the destination
    # it will determine which currencies to convert from and to. It offers 
    # the most likely currency conversion but also allows the user to pick
    # what to convert.
#Return value:
    # Void
    if destination == "Tokyo":
        answer = input("Would you like to convert to from USD to Yen? ")
        if answer == "yes" or answer == "Yes":
            amount = float(input("How much would you like to convert (enter number)? "))
            US_Yen(amount, "US to Yen")
        else:
            convert = input("What would you like to convert? ")
            amount = float(input("How much would you like to convert (enter number)? "))
            if "US" in convert:
                backup_1(amount, convert)
            else:
                backup_2(amount, convert)
    elif destination == "London":
        answer = input("Would you like to convert to from USD to Pound? ")
        amount = float(input("How much would you like to convert (enter number)? "))
        if answer == "yes" or answer == "Yes":
            US_Pound(amount, "US to Pound")
        else:
            convert = input("What would you like to convert? ")            
            if "US" in convert:
                backup_1(amount, convert)
            else:
                backup_2(amount, convert)
    elif destination == "Rome":
        answer = input("Would you like to convert to from USD to Euro? ")
        amount = float(input("How much would you like to convert (enter number)? "))
        if answer == "yes" or answer == "Yes":
            US_Euro(amount, "US to Euro")
        else:
            convert = input("What would you like to convert? ")
            if "US" in convert:
                backup_1(amount, convert)
            else:
                backup_2(amount, convert)   
    else:
        print("You do not need to convert.")

def US_Pound(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts USD to Pound or vise versa.
#Return value:
    # Void
    if convert == "US to Pound":
        pound = round((0.81*amount),2)
        print("£" + str(pound))
    elif convert == "Pound to US":
        dollar = round((1.24*amount),2)
        print("$" + str(dollar))

def US_Yen(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts USD to Yen or vise versa.
#Return value:
    # Void
    if convert == "US to Yen":
        yen = round((107.47*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to US":
        dollar = round((0.0093*amount),2)
        print("$" + str(dollar))

def US_Euro(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts USD to Euro or vise versa.
#Return value:
    # Void
    if convert == "US to Euro":
        euro = round((0.92*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to US":
        dollar = round((1.08*amount),2)
        print("$" + str(dollar))

def Pound_Euro(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts Euro to Pound or vise versa.
#Return value:
    # Void
    if convert == "Pound to Euro":
        euro = round((1.14*amount),2)
        print("€" + str(euro))
    elif convert == "Euro to Pound":
        pound = round((0.87*amount),2)
        print("£" + str(pound))

def Pound_Yen(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts Yen to Pound or vise versa.
#Return value:
    # Void
    if convert == "Pound to Yen":
        yen = round((132.89*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Pound":
        pound = round((0.0075*amount),2)
        print("£" + str(pound))
    
def Euro_Yen(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # converts Euro to Yen or vise versa.
#Return value:
    # Void
    if convert == "Euro to Yen":
        yen = round((116.31*amount),2)
        print("¥" + str(yen))
    elif convert == "Yen to Euro":
        euro = round((0.0086*amount),2)
        print("€" + str(euro))

def backup_1(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # If user wants to convert a different currency it calls appropriate fnc.
#Return value:
    # Void
    if "US" and "Euro" in convert:
        US_Euro(amount, convert)
    elif "US" and "Pound" in convert:
        US_Pound(amount, convert)
    elif "US" and "Yen" in convert:
        US_Yen(amount, convert)
    else:
        print("Cannot convert this currency")    

def backup_2(amount, convert):
# Parameters: 
    # amount: amount of money to convert.
    # convert: string of which currencies to convert.
#Function purpose:
    # If user wants to convert a different currency it calls appropriate fnc.
#Return value:
    # Void
    if "Pound" and "Euro" in convert:
        Pound_Euro(amount, convert)
    elif "Euro" and "Yen" in convert:
        Euro_Yen(amount, convert)
    elif "Yen" and "Pound" in convert:
        Pound_Yen(amount, convert)
    else:
        print("Cannot convert this currency")
