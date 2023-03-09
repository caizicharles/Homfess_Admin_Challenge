# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:12:19 2023

@author: yannd
"""

from reply_data_cleaning import *
import pandas as pd
import numpy as np

grid_array = np.array(grid())

def grid_to_df():
    grid_array = np.array(grid())
    df = pd.DataFrame(grid_array)
    return df

def initial_coordinate():
    ''' returns coordinates (tuple) of each block we want to colour'''
    df = grid_to_df()
    df_sum_col = df.sum(axis=1)
    
    max_col_idx = df_sum_col.idxmax()
    
    # Now we have the index of the largest sum row
    # We want to see the column of the largest value on that row
    max_row_idx = df.loc[max_col_idx].idxmax()
    
    return [max_col_idx, max_row_idx]

def next_block(prev_coord):
    '''given a dataframe and the previous coordinate, returns the next coordinate
    which maximises the gains'''
    
    df = grid_to_df()
    row_init, col_init = prev_coord
    
    ## Manually check the 4 squares around
    ## If time, code a function to make this more readable
    ## Set Block up as initial values
    try:
        max_val = df.loc[row_init][col_init-1]
        max_coord = [row_init, col_init-1]
    except:
        max_val = df.loc[row_init][total_cols-1]
        max_coord = [row_init, total_cols-1]
    
    # Check block right
    try:
        if df.loc[row_init][col_init+1] > max_val:
            max_val = df.loc[row_init][col_init+1]
            max_coord = [row_init, col_init+1]
    except:
        if df.loc[row_init][0] > max_val:
            max_val = df.loc[row_init][0]
            max_coord = [row_init, 0]
            
    # Check block top
    try:
        if df.loc[row_init-1][col_init] > max_val:
            max_val = df.loc[row_init-1][col_init]
            max_coord = [row_init-1, col_init]
    except:
        if df.loc[total_rows-1][col_init] > max_val:
            max_val = df.loc[total_rows-1][col_init]
            max_coord = [total_rows-1, col_init]
            
    # Check block down
    try:
        if df.loc[row_init+1][col_init] > max_val:
            max_val = df.loc[row_init+1][col_init]
            max_coord = [row_init+1, col_init]
    except:
        if df.loc[0][col_init] > max_val:
            max_val = df.loc[0][col_init]
            max_coord = [0, col_init]
            
    ## include overlap fct in each to choose
    return max_coord

def record_path(snake_length):
    df = grid_to_df()
    path = []
    current_pos = initial_coordinate()
    for length in range(snake_length):
        path.append(current_pos)
        current_pos = next_block(current_pos)
        
    return path
        
    
