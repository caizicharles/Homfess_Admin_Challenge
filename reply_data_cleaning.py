# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:23:56 2023

@author: yannd
"""

f = open('example.txt', 'r')
lines = f.readlines()
data = []

# Read and clean data
for line in lines:
    liste = line.split()
    int_liste = [int(idx) for idx in liste]
    data.append(int_liste)
    
print(data)
<<<<<<< HEAD
#this is printing
=======
    
>>>>>>> origin/main
