def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    i = 0
    a = []
    while i < len(score):
        a.append(score[i])
        if len(a) == m:
            answer += min(a) * m
            a = []
        i += 1

    return answer


"""
나누는게 뭐 있었지 했는데 :: 슬라이싱 스탭

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m # 제일 작은 앞부분 제외하고 시작
-----------------------------------------------
def solution(k, m, score):
    result = 0
    score.sort(reverse = True)
    for i in range(m - 1, len(score), m):
        result += score[i] * m

    return result
"""
