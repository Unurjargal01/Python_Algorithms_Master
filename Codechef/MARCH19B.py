import numpy as np
for _ in range(int(input())):
    N = int(input())
    A = np.array(list(map(int, input().split())))
    Z = list(filter(lambda x: x > 0, [sum(A < 0),  sum(A > 0)]))
    print(min(Z), max(Z))