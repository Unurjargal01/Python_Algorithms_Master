from collections import defaultdict
def leaps (G, u, lent = 0, t = list()):
    if not u in G.keys(): return [lent]
    for i in G[u]:
        #print(i, t)
        t.extend(leaps(G, i, lent + 1, t = list()))
    t.append(lent)
    return t

def deg(param, x, i, mod):
    t = param % mod
    for j in range(i):
        t = (t * (x % mod)) % mod
    return t

for _ in range(int(input())):
    N, Q = map(int, input().split())
    mod = 10 ** 9 + 7
    G_to = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G_to[u].append(v)
    ans = 0

    while Q != 0:
        a, b = map(int, input().split())
        v, y = a ^ ans, b ^ ans
        #print(v, y)
        ans = 0
        k = sorted(leaps(G_to, v, t = list()))
        #print(k)
        for i in range(len(k)):
            ans = (ans + deg(k[i], y, i, mod)) % mod 
        print(ans)
        Q -= 1