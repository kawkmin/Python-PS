def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            answer.append(i-s[:i].rfind(s[i]))
        else:
            answer.append(-1)
    return answer


'''
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
'''
