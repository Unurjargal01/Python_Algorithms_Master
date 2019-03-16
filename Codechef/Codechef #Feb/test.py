# ARTBALAN.py
from collections import Counter
from itertools import filterfalse
import numpy as np 

def factor(s):
    t = {i for i in range(1, s // 2 + 1) if s % i == 0}
    t.add(s)
    return t
for _ in range(int(input())):
    s = input()
    Elements = np.array(list(Counter(s).values())a)

    #print(min([sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, sorted(Elemenets - i)))))[:(int(len(s) / i) - sum((Elemenets - i) >= 0))]) for i in factor(len(s))]))
    print([sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, sorted(Elements - i)))))[:(int(len(s) / i) - sum((Elemenets - i) >= 0))]) for i in factor(len(s))])
# filterfalse
    for i in factor(len(s)):
        
        
        
        
        filterfalse(Elements - i # element nemeh yostoi ehelj - baigaagaa duurgeed uldsen hed deer ni 
    





"""
# HMAPPY2.py
from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)
for _ in range(int(input())):
    N, A, B, K = map(int, input().split())

    list_ =   len(range(0, N, A)) + len(range(0, N, B)) - 2 * len(range(0, N, lcm(A, B))) 

    print( list_ , N // A + N // B - 2 * N / lcm (A, B)) 

    print( list_ , N // A + N // B - 2 * N // lcm (A, B)) 

    print(len(range(1, N + 1, A)), N // A)
    print(len(range(1, N + 1, B)), N // B)
    print(len(range(1, N + 1, lcm(A, B))), N // lcm(A, B))
    
"""

