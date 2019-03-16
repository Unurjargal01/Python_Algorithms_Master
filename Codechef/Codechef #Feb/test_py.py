from collections import Counter
from itertools import filterfalse
import numpy as np 

def factor(s):
    t1 = {i for i in range(1, s // 2 + 1) if s % i == 0}
    t1.add(s)
    return t1

for _ in range(int(input())):
    s = input()

    Elements = np.array(list(Counter(s).values()))
    Answer = set()
    #print(Elements)
    for i in factor(len(s)):
        if (len(s) // i) <= len(Elements):
            Answer.add( sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, Elements - i))))[:(len(s) // i - sum((Elements - i) >= 0))]))
            #Answer.add((i, 'UP', sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, Elements - i))))[:(len(s) // i - sum((Elements - i) >= 0))])))
        else:
            Answer.add(len(s) - len(list(filterfalse(lambda x: x < 0, Elements - i))) * i)   
            #Answer.add((i, "DOWN", len(s) - len(list(filterfalse(lambda x: x < 0, Elements - i))) * i))     
    #print(Answer)
    print(min(Answer))