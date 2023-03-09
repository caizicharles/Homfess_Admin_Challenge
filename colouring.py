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

data_df = grid_to_df()

def initial_coordinate(df):
    ''' returns coordinates (tuple) of each block we want to colour'''
    df_sum_col = df.sum(axis=1)
    
    max_col_idx = df_sum_col.idxmax()
    
    # Now we have the index of the largest sum row
    # We want to see the column of the largest value on that row
    max_row_idx = df.loc[max_col_idx].idxmax()
    
    return (max_row_idx, max_col_idx)

def next_block(df, prev_coord):
    '''given a dataframe and the previous coordinate, returns the next coordinate
    which maximises the gains'''
    
    row_init, col_init = prev_coord
    print(row_init, col_init)
    max_val = 0
    max_val = df.loc[row_init][col_init]
    max_coord = prev_coord
    
    ## Manually check the 4 squares around
    ## Set Block up as initial values
    max_val = df.loc[row_init][col_init-1]
    max_coord = [row_init][col_init-1]
    
    # Check block down
    if df.loc[row_init][col_init+1] > max_val:
        max_val = df.loc[row_init][col_init+1]
    
    
    
    
    
    
    
    
    
    
    # return None
    
