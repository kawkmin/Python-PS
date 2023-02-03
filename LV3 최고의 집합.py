def solution(n, s):
    if n > s:
        return [-1]

    x = s // n
    y = s % n

    li = [x] * n
    for i in range(y):
        li[i] += 1

    return sorted(li)


# 모든 리시트의 가장 큰 곱의 값이 되려면, 균등하게 커야함
