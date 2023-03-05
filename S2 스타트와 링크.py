def dfs(x, dep):
    global MIN
    if dep == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    a += s[i][j]
                elif not visit[i] and not visit[j]:
                    b += s[i][j]
        MIN = min(MIN, abs(a - b))
        return

    for i in range(x, n):
        if not visit[i]:
            visit[i] = True
            dfs(i + 1, dep + 1)
            visit[i] = False


n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]
visit = [False for _ in range(n)]
MIN = int(1e9)
dfs(0, 0)
print(MIN)
