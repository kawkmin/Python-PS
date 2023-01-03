def solution(n):
    temp_list=list(str(n)[::-1])
    answer=[]
    for i in temp_list:
        answer.append(int(i))
    return answer

'''
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
'''