# 틀렸는데 똑같은 C++에선 가능

n, m = map(int, input().split())

if m == 0:
    s = []
else:
    s = list(map(int, input().split()))

MIN = int(1e9)
li = []
for x in range(1002):
    if x not in s:
        li.append(x)

for i in li:
    for j in li:
        for k in li:
            MIN = min(MIN, abs(n - (i * j * k)))

    if MIN == 0:
        break

print(MIN)
