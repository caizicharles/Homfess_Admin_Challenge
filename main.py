import numpy as np
import reply_data_cleaning as rdc
#import colouring as col
#import update as up
#import overlap_check as check

def pre_processing(S_num, S_length):
    Snakes_list = []

    for i in range(0, S_num):
        s = np.array([[2,2]])
        for j in range(0, S_length[i]-1):
            s = np.concatenate((s, np.array([[0,0]])))
        each_snake = np.array(s)
        Snakes_list.append(each_snake)
    
    return np.array(Snakes_list)


def main():
    input = np.array(rdc.input())

    #Map properties
    R = input[0][0]
    C = input[0][1]
    grid = np.array(input[2:])
    print(grid)

    #Snake properties
    S_num = input[0][2]
    S_length = input[1]
    Snakes = pre_processing(S_num, S_length)

    iter_num = 20
    #eta = 

    


    return None

main()
