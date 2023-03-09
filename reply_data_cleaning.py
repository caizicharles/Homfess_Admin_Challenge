# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:23:56 2023

@author: yannd
"""

def input():
    f = open('example.txt', 'r')
    lines = f.readlines()
    data = []

    # Read and clean data
    for line in lines:
        liste = line.split()
        int_liste = []
        for idx in liste:
            try:
                int_liste.append(int(idx))
            except:
                int_liste.append(-1)
        data.append(int_liste)
    

    return data

def output():
    
    return None
