from collections import defaultdict
def leaps (G, u, lent = 0, t = list()):
    if not u in G.keys(): return [lent]
    for i in G[u]:
        print(i, t)
        t.extend(leaps(G, i, lent + 1, t = list()))
    t.append(lent)
    return t

for _ in range(int(input())):
    N, Q = map(int, input().split())
    mod = 10 ** 9 + 7
    G_to = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G_to[u].append(v)

    print(leaps(G_to, 1))