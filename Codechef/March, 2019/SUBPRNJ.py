import math
from collections import Counter
def insert_sort(seq, elem, i = None):
    if i is None: i = len(seq)
    j = i
    seq.append(elem)
    while j and seq[j] < seq[j - 1]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1
for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        S = []
        t = i
        C = Counter()
        set_ = set(C.keys())
        while t != N :
            insert_sort(S, A[t])
            if not A[t] in C.keys():
                C[A[t]] = 1
                set_.add(A[t])
            else:
                C[A[t]] += 1
            dif = set_ & set(C.values())
            if dif:
                kth = S[math.ceil(K / math.ceil(K / len(S))) - 1] # sorted
                if C[kth] in dif:
                    answer += 1
            t += 1
            
    print(answer)   
"""
    1
7 9
1 2 79 9 9 5 7 6 5 9
2 5 9 9 79
"""
