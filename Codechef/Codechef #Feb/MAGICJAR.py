import numpy as np
for _ in range(int(input())):
    N = int(input())
    print(sum(np.array(list(map(int, input().split()))) - 1) + 1)