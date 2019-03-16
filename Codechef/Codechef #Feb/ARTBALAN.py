from collections import Counter
from itertools import filterfalse
import numpy as np 

def factor(s):
    t = {i for i in range(1, s // 2 + 1) if s % i == 0}
    t.add(s)
    return(t)

for _ in range(int(input())):
    s = input()
    _list = np.array(list(Counter(s).values()))        
    
    #print(min([sum(sorted(np.abs(_list - i))[:int((len(s) / i) - sum((_list - i) > 0))]) for i in factor(len(s))]))
    
    #print(min([sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, sorted(_list - i)))))[:int((len(s) / i) - sum((_list - i) >= 0))]) for i in factor(len(s))]))
    if sum(_list - 1) == 0:
        print(0)
    else:
        print(min([sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, sorted(_list - i)))))[:int((len(s) / i) - sum((_list - i) >= 0))]) for i in factor(len(s))]))
        print([sum(sorted(np.abs(list(filterfalse(lambda x: x >= 0, sorted(_list - i)))))[:int((len(s) / i) - sum((_list - i) >= 0))]) for i in factor(len(s))])
    
    for i in factor(len(s)):
        print(i)
        print(sorted(_list - i))
        print(np.abs(list(filterfalse(lambda x: x >= 0, sorted(_list - i)))))
        
    # abcdefgadk
    #print([sum(sorted(np.abs(_list - i))[:(len(s) // i)]) for i in factor(len(s))])
    # aabcdeqafsda - a: 4; d: 2; c: 1; b: 1; e: 1; f: 1; s: 1; q: 1;
    # bceqafsa --> bceqcfsa --> bceqcfsb --> bceqcesb --> bcescesb