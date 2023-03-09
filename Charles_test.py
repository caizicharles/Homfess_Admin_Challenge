import numpy as np

Snakes = []
print("hi")
print(Snakes)
print("hi")
S_num = 2
S_length = [2,3]

for i in range(0, S_num):
    s = np.array([[2,2]])
    for j in range(0, S_length[i]-1):
        s = np.concatenate((s, np.array([[0,0]])))
    each_snake = np.array(s)
    Snakes.append(each_snake)
print(np.array(Snakes))
print(Snakes[0])

