import numpy as np

# snake_counter, colour_counter
# every time colouring function colours a square, colour_counter += 1

M = np.array([[]])
restart = 0

def overlap_checker():
    S = snakes[snake_counter]
    coord = S[colour_counter]
    np.concatenate(M,coord)
    u = coord + [-1,0]
    d = coord + [1,0]
    r = coord + [0,1]
    l = coord + [0,-1]
    if u[0] == -1:
        u[0] = R
    if d[0] == R +1:
        d[0] = 0
    if r[1] == C + 1:
        r[1] = 0
    if l[1] == -1:
        l[1] = C
    adjacents_available = []
    if u in M.tolist()==False:
        adjacents_available.append(u)
    if d in M.tolist()==False:
        adjacents_available.append(d)
    if l in M.tolist()==False:
        adjacents_available.append(l)
    if r in M.tolist()==False:
        adjacents_available.append(r)
    if len(adjacents_available) == 0:
        restart = 1 
    return adjacents_available, restart

