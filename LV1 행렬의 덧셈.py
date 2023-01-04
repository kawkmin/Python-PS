def solution(arr1, arr2):
    answer = []
    for i,a in enumerate(arr1):
        li=[]
        for j,b in enumerate(a):
            li.append(b+arr2[i][j])
        answer.append(li)
        
    return answer

'''
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A
'''
'''
def solution(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
'''