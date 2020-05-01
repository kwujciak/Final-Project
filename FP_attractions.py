#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:48:45 2020

@author: katewujciak
"""

import numpy as np
import pandas as pd

attractions = pd.read_csv("attractions.csv")
att = np.array(attractions)
locations = att[:,0]
att_list = att[:,1]
print(locations)


location = input("What would you like to travel? ")

def attract():
    index = np.where(locations == location)
    print(index)
#    if location in locations:
#        value_index = locations.index(location)
#        print(value_index)
attract()

    


#def readcsv(filename):	
#    att = open(filename, "rU")
#    reader = csv.reader(att, delimiter=";")
#
#    rownum = 0	
#    a = []
#
#    for row in reader:
#        a.append (row)
#        rownum += 1
#    
#    att.close()
#    print(a)
#    return a
#readcsv("attractions.csv")

#attractions =  np.loadtxt('attractions.csv', delimiter=',', skiprows=1, unpack=True)
#
#print(attractions)

#import csv
#
#with open('attractions.csv', newline='') as attractions:
#    att = csv.reader(attractions, delimiter=' ', quotechar='|')
#    for row in att:
#        print(row['London'])