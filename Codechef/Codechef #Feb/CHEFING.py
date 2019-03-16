for _ in range(int(input())): 
    A = set()
    for i in range(int(input())):
        t = input()
        A = [A & set(t), set(t)][i == 0]

    print(len(A))
