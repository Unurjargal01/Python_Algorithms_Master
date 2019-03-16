    def Rec(x, new):
        k = len(x)
        if k == 0:
            return [new]
        if k == 1:
            if x[0][0] >= new[0]:
                return [new] + x
            else:
                return x + [new]

        k = len(x) // 2
        if x[k][0] >= new[0]:
            return Rec(x[:k], new) + x[k:]
        else:
            return x[:k] + Rec(x[k:], new)

    """
    def Rec_1(x, new):
        if new[0] >= x[-1][0]:
            return x + [new]
        for i in range(len(x) - 1, -1, -1):
            if x[i - 1][0] <= new[0] <= x[i][0]:
                return x[:i] + [new] + x[i:]
    """
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = []
    for i in range(len(A)):
        x = Rec(x, [A[i] * B[i], B[i]])

    for _ in range(M):
        x[-1][0] = x[-1][0] - x[-1][1] 
        x = Rec(x[:-1], x[-1])
        #print(x)


    print(x[-1][0])

