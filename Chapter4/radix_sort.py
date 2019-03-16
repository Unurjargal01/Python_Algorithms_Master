def full(element, length):
    return '0' * (length - len(element)) + element
def naive_radix(seq):
    max_ = len(str(max(map(int, seq))))
    seq = [full(i, max_) for i in seq]
    for i in range(max_ - 1, -1, -1):
        seq.sort(key = lambda  x: int(x[i]))
        print(seq)
    return seq
def radix(seq, max_ = None):
    if max_ is None: max_ = len(str(max(map(int, seq))))
    for i in range(max_ - 1, -1, -1):
        try:
            seq.sort(key = lambda x: int(x[i]))
        except:
            
print(naive_radix(list(input().split())))


