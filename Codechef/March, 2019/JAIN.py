from collections import defaultdict
for _ in range(int(input())):
    dict_ = defaultdict(int)
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    N = int(input())
    for _ in range(N):
        dict_["".join(set(input()))] += 1
    counter, counter1 = 0, 0
    if "".join(vowels) in dict_:
        t = dict_["".join(vowels)]
        counter1 = t * ((sum(dict_.values()) - (t + 1) / 2)) 
        del dict_["".join(vowels)]
    key = list(dict_.keys())
    for i in range(len(key) - 1):
        for j in range(i + 1, len(key)):
            if (set(key[i]) | set(key[j])) == vowels:
                counter += dict_[key[i]] * dict_[key[j]]
                
    counter += int(counter1)
    print(counter)