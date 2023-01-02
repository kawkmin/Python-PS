def solution(s):
    answer = 0
    data = s.split(" ")
    i=len(data)-1
    while i>=0:
        if data[i]=="Z":
            answer-= int(data[i-1])*2
        else :
            answer+=int(data[i])
        i-=1
            
    return answer

print(solution("1 2 Z 3"))