def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    q.append((0, 0, 1))
    xsize = len(maps[0])
    ysize = len(maps)

    while len(q) != 0:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax >= 0 and ay >= 0 and ax < xsize and ay < ysize and maps[ay][ax] == 1:
                maps[ay][ax] = maps[y][x] + 1
                q.append((ax, ay))

    if maps[-1][-1] != 1:
        return maps[-1][-1]

    return -1
