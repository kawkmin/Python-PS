import math
def solution(n):
    answer = 0
    for i in range(1,int(math.sqrt(n))+1):
        for j in range(i,n+1):
            if i*j==n:
                if i==j:
                    answer+=i
                else:
                    answer+=i+j
                continue
                
    return answer

'''
def solution(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
'''