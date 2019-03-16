def solve(seq, digit, counter = 0):
    if len(seq) == 0: return counter * digit 
    set_ = set(seq) 
    if digit <= min(set_): 
        return (len(seq) + counter) * digit #str??
    else:
        for i in range(len(seq)):
            if seq[i] == min(set_):
                return seq[i] + solve(seq[(i + 1):], digit, counter + i)
    
for _ in range(int(input())):
    N, d = input().split()

    print(solve(N, d))