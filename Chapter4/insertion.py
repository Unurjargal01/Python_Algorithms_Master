def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1

def rec_ins_sort(seq, i):
    if i == 0: return 
    rec_ins_sort(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1

def insert_sort(seq, elem, i = None):
    if i is None: i = len(seq)
    j = i
    seq.append(elem)
    while j and seq[j] < seq[j - 1]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1

seq = [1, 2, 3, 5, 6]
insert_sort(seq, 4)
print(seq)
