import numpy as np

# snake_counter, colour_counter
# every time colouring function colours a square, colour_counter += 1

M = np.array([[]])
restart = 0

def overlap_checker():
    S = snakes[snake_counter]
    coord = S[colour_counter]
    np.concatenate(M,coord)
    adjacents_available = []
    up_adjacent = coord + [0,1]
    down_adjacent = coord + [0,-1]
    right_adjacent = coord + [1,0]
    left_adjacent = coord + [-1,0]
    if up_adjacent in M.tolist()==False:
        adjacents_available.append(up_adjacent)
    if down_adjacent in M.tolist()==False:
        adjacents_available.append(down_adjacent)
    if left_adjacent in M.tolist()==False:
        adjacents_available.append(left_adjacent)
    if right_adjacent in M.tolist()==False:
        adjacents_available.append(right_adjacent)
    if len(adjacents_available) == 0:
        restart = 1 
    return adjacents_available, restart

