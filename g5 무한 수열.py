from collections import defaultdict


def dp(x):
    global a, p, q
    if a[x] > 1 or x == 0:
        return a[x]
    else:
        a[x] = dp(x // p) + dp(x // q)
        return a[x]


n, p, q = map(int, input().split())
a = defaultdict(int)
a[0] = 1
print(dp(n))
