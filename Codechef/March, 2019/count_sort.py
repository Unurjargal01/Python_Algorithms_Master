from collections import defaultdict
def count(seq):
    dict_ = defaultdict(list)
    List = []
    for i in seq:
        dict_[i].append(i)
    for i in range(min(dict_.keys()), max(dict_.keys()) + 1):
        List.extend(dict_[i])
    return List
    