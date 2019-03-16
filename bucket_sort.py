from collections import defaultdict
from insertion import insertion_sort
def bucket_sort(seq, n):
    step = 1 / n
    s = []
    for i in range(n):
        t = [j for j in seq if (j >= step * i) and (j <= step * (i + 1))]
        insertion_sort(t)
        s.extend(t)
    return s
    
print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68], 10))