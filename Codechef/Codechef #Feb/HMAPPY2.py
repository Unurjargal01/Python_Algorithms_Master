from math import gcd
def lcm(x, y):
    return x * y // gcd(x, y)

for _ in range(int(input())):
    N, A, B, K = map(int, input().split())
    print(['Lose', 'Win'][(N // A + N // B - 2 *  N // lcm(A, B)) >= K])
    print(N // A + N // B - 2 *  N // lcm(A,  B))
