from copy import copy
import numpy as np
def check(tup, Result_Case):
    for x, y in Result_Case:
        if (abs(x - tup[0]) == abs(y - tup[1])):
            return False

    return True

def Rec(a, Result, row = 0, Result_Case = []):
    for i in a:
        if (check((i, row), Result_Case)):
            b = copy(a)
            b.remove(i)
            Rec(b, Result, row + 1, Result_Case + [(i, row)])
    
    if not a:
        Result += [Result_Case]
Result = []
a = list(range(8))
Rec(a, Result)
print(len(Result))
# Print results with the form of table
for i in Result:
    table = np.zeros([8, 8])
    for x, y in i:
        table[x][y] = 1
    print(table)
