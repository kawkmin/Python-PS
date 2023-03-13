n = int(input())

li = []
for _ in range(n):
    li.append(tuple(map(int, input().split())))

li = sorted(li, key=lambda x: (x[1], x[0]))
print(li)

cnt = 0
t = 0
for x in li:
    if x[0] >= t:
        t = x[1]
        cnt += 1

print(cnt)
