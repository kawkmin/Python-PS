# 처음부터 모든 계산 다 하려고함.
def solution(dartResult):
    answer = 0
    index = -1
    dic = {'S': 1, 'D': 2, 'T': 3}
    result_list = []
    minus_list = [1]*4
    multi_list = [1]*4
    i = 0

    while i < len(dartResult):
        if dartResult[i].isdigit():
            if dartResult[i+1] == '0':
                result_list.append(
                    int(dartResult[i:i+2])**dic[dartResult[i+2]])
                i += 2
                index += 1
            else:
                result_list.append(int(dartResult[i])**dic[dartResult[i+1]])
                i += 1
                index += 1

        elif dartResult[i] == '*':
            if index > 0:
                if multi_list[index-1] == 2:
                    multi_list[index-1] = 4
                else:
                    multi_list[index-1] = 2

            multi_list[index] = 2

        elif dartResult[i] == '#':
            minus_list[index] = -1

        i += 1

    for i in range(len(result_list)):
        result_list[i] = result_list[i]*minus_list[i]*multi_list[i]

    return sum(result_list)


'''
숫자를 맨 처음으로 분류함
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult] 
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
'''

'''
파이썬 -로 뒤에서부터 계산가능 이용함.
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)
'''
