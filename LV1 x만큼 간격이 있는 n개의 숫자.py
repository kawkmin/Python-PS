def solution(x, n):
    answer=[]
    a=0
    for i in range(1,n+1):
        a+=x
        answer.append(a)
    return answer

'''
def solution(x, n):
    return [i*x+x for i in range(n)]
'''