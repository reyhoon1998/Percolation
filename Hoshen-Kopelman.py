import numpy as np
import matplotlib.pyplot as plt

length = np.array([10, 100, 200])
probability = np.arange(0, 1, 0.05)
iteration = 100
experiments = np.zeros((len(length), len(probability), iteration))
probability_Q = np.zeros((len(length), len(probability), iteration))


def Hoshen_Keoplman(length, prob):
    network = np.zeros((length, length), dtype=int)
    network[:, 0] = 1
    l = np.zeros(length * length, dtype=int)
    s = np.zeros(length * length, dtype=int)
    l[1] = 1
    s[l[1]] = length
    number = 2
    for j in range(1, length):
        for i in range(1, length):
            if np.random.random() < prob:
                left = network[i, j - 1]
                up = network[i - 1, j]
                if left == 0 and up == 0:
                    network[i, j] = number
                    l[number] = number
                    s[l[number]] += 1
                    number += 1

                elif left != 0 and up == 0:
                    network[i, j] = left
                    s[l[left]] += 1
                elif up != 0 and left == 0:
                    network[i, j] = up
                    s[l[up]] += 1

                elif l[up] == l[left]:
                    network[i, j] = left
                    s[l[left]] += 1
                else:
                    network[i, j] = left
                    s[l[left]] = (s[l[left]] + s[l[up]] + 1)
                    s[l[up]] = 0
                    l[l == l[up]] = l[left]

    return int(l[1] in l[network[:, length-1]]), l, s


for i in range(len(length)):
    print(length[i])
    for k in range(len(probability)):
        for j in range(iteration):
            q, l, s = Hoshen_Keoplman(length[i], probability[k])
            experiments[i, k, j] = q
            if q == 1:
                probability_Q[i, k, j] = (s[l[1]] - length[i]) / (np.sum(s) - length[i])

acc = np.mean(experiments, axis=2)
acc2 = np.mean(probability_Q, axis=2)
for i in range(len(length)):
    plt.plot(probability, acc2[i], '.-')
plt.xlabel('probability')
plt.ylabel('Q_inf')
plt.show()
