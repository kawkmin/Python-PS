import math
def solution(n):
    if int(math.sqrt(n)) == math.sqrt(n) :
        return math.pow(int(math.sqrt(n))+1,2)
    else : 
        return -1

'''
def solution(n):
    return -1 if n**.5 % 1 else (n**.5+1)**2
'''