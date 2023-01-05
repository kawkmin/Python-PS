def solution(arr):
    answer = []
    x = 1
    for i, a in enumerate(arr):
        if i == 0:
            answer.append(a)
            x = a
        else:
            if x != a:
                x = a
                answer.append(a)
    return answer


'''
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''
