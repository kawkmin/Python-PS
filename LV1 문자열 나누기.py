# 생성이 완료된 시점을 기준으로 잡았음
def solution(s):
    answer = 0
    dic = {}
    x = ""
    nx = 0
    b = False
    for i in s:
        b = False
        if x == "":
            x = i
            dic[x] = 1
        elif i == x:
            dic[x] += 1

        else:
            nx += 1
            if dic[x] == nx:
                answer += 1
                x = ""
                dic = {}
                nx = 0
                b = True

    if not b:
        answer += 1

    return answer


"""
생성되는 시점을 기준으로 잡았음
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
"""
