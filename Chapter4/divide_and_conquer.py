def div(seq):
    if len(seq) == 1: return seq
    mid = len(seq) // 2
    lsq = div(seq[:mid])
    rsq = div(seq[mid:])
    S = []

    while lsq and rsq:
        if lsq[-1] >= rsq[-1]:
            S.append(lsq.pop())
        else:
            S.append(rsq.pop())
    S.reverse()
    return (lsq or rsq) + S

print(div(list(map(int, input().split()))))
