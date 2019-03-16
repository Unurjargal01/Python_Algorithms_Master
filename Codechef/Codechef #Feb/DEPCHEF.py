for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    t = -1
    for i in range(N):
        if (D[i] - A[i - 1] - A[(i + 1) % N]) > 0:
            if t < D[i]:
                t = D[i]
            
    print(t) 