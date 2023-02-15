def solution(brown, red):
    answer = []

    for i in range(1, red // 2 + 2):
        if red % i == 0:
            a = max(red // i, i)
            b = min(red // i, i)
            if a * 2 + (b + 2) * 2 == brown:
                answer.append(a + 2)
                answer.append(b + 2)
                break
    return answer
