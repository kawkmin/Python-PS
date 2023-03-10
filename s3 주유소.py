n = int(input())
dis = list(map(int, input().split()))
node = list(map(int, input().split()))

i = 0
result = 0

while i < n - 1:
    temp = i
    result += node[i] * dis[i]
    for j in range(i + 1, n - 1):
        if node[j] > node[temp]:
            result += node[temp] * dis[j]
            i += 1
        else:
            break
    i += 1

print(result)

""" 식을 만들 생각을 하지 않음. 무조건 순서적으로만 생각
m = node[0]
for i in range(n - 1):
    if m > node[i]:
        m = node[i]
    result += m * node[i]
print(result)
"""
