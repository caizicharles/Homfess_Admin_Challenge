import numpy as np

'''Snakes = 
S_num = 2
S_length = [2,3]

for i in range(0, (S_num-1)):
    for j in range(0, S_length[i]-1):
        s = np.array([[0,0]])
        s = np.concatenate((s, np.array([[0,0]])))
    Snakes.append(np.array(s))
print(Snakes)'''

a = np.array([[0,0]])
print(a)
b = np.array([[0,0]])
print(np.concatenate((a,b)))
