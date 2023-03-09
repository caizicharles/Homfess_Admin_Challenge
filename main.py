import numpy as np
import reply_data_cleaning as rdc

def pre_processing():
    return None


def main():
    input = np.array(rdc.input())

    R = input[0][0]
    C = input[0][1]
    grid = np.array(input[2:])
    S_num = input[0][2]
    S_length = input[1]
    iter_num = 20
    #eta = 

    Snakes = []

    for i in range(0, S_num):
        for j in range(0, S_length[i]):
            Snakes.append([0,0])
    Snakes = np.array(Snakes)



    return None

#main()
