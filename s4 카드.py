import sys
from collections import defaultdict

dic = defaultdict(int)

for _ in range(int(input())):
    dic[int(sys.stdin.readline().strip())] += 1

dic = sorted(dic.items(), key=lambda x: x[0])
dic = sorted(dic, key=lambda x: x[1], reverse=True)
print(dic[0][0])
