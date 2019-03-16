import numpy as np

def table(tab):
    table[N][M] = tab[N - 1][M] + tab[N][M - 1]


for _ in range(int(input())):
    N = np.array([int(i) for i in input()])
    M = np.array([int(i) for i in input()])

    Table = np.zeros([N + 1, M + 1])
    Table[0][:] = N
    Table[:][0] = 
    for _ in range(int(input()):