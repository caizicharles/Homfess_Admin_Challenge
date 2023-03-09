import numpy as np

'''Snakes = np.array([[1,1]])
S_num = 2
S_length = [2,3]

for i in range(0, S_num):
    for j in range(0, S_length[i]-1):
        s = np.array([[0,0]])
        s = np.concatenate((s, np.array([[0,0]])))
    Snakes = np.concatenate((Snakes, np.array(s)))
print(Snakes)

a = np.array([[0,0],[0,0]])
b = np.array([[0,0]])
a = np.concatenate((a,b))
print(a)'''

a = [[0],[1],[2]]
print(np.array(a[1:]))
