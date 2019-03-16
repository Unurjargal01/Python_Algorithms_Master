# binary search
from collections import deque
def check(seq, K):
    count = 0
    for i in range(1, len(seq) + 1):
        count += seq[i - 1] // i
    if count <= K: return True
    else: return False
for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    T = deque()
    for i in range(N, 0, -1):
        T.appendleft(A.pop())
        if check(T, K):
            print(N + 1 - i)
            break        
    else:
        print(N + 1)