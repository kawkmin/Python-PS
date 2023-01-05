def solution(s):
    answer = ''
    li = s.split(" ")

    for i in range(len(li)):
        for j in range(len(li[i])):
            if j % 2 == 0:
                answer += li[i][j].upper()
            else:
                answer += li[i][j].lower()
        answer += ' '
    return answer[:-1]
