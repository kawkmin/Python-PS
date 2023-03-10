import sys

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    a = sys.stdin.readline().split()
    dic[a[0]] = a[1]

for _ in range(m):
    print(dic[input()])
