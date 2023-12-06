import random
import numpy as np
import matplotlib.pyplot as plt

length = 100
network = np.zeros((length, length))  # 2D lattice
color = np.zeros((length, length))
network[:, 0] = 1  # Setting one for value of all nodes on the left
probability = 0.8


def coloring():
    number = 2
    for i in range(1, length):
        for j in range(1, length):
            if random.random() < probability:
                # if the node is on, check up and left neighbor
                up = network[j, i - 1]
                left = network[j - 1, i]
                if up == 0 and left == 0:
                    # if neighbors are off, the new value set for the node
                    network[j, i] = number
                    number += 1
                    # if one of the neighbors is non-zero, its value set to the node
                elif up != 0 and left == 0:
                    network[j, i] = up
                elif up == 0 and left != 0:
                    network[j, i] = left
                else:
                    # if the two neighbors are non-zero, the minimum set to the node
                    # all nodes with another value, get this value
                    min_number = min(up, left)
                    network[j, i] = min_number
                    mask_number1 = (network == up)
                    mask_number2 = (network == left)
                    final = mask_number1 | mask_number2
                    network[final] = min_number
    # if number one exists in the last column, return 1, meaning the percolation exists.
    return network, int(1 in network[:, -1])


my_network, Q = coloring()
print(Q)
plt.imshow(my_network)
plt.show()
