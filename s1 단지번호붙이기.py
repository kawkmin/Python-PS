def dfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global board, visit, a, n
    a += 1
    for z in range(4):
        x = dx[z] + j
        y = dy[z] + i
        if (
            x >= 0
            and y >= 0
            and x < n
            and y < n
            and board[y][x] == 1
            and visit[y][x] == 0
        ):
            visit[y][x] = 1
            dfs(y, x)


n = int(input())
board = [list(map(int, input())) for _ in range(n)]
result = []

visit = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visit[i][j] == 0:
            a = 0
            visit[i][j] = 1
            dfs(i, j)
            result.append(a)

print(len(result))
for i in sorted(result):
    print(i)
