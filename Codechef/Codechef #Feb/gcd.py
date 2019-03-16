def gcd(x, y):
    while x != 0:
        x, y = min(x, y % x), max(x, y % x)
    return y

print(gcd(10, 25))
