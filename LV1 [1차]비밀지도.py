def to_binary(x, n):
    temp = []
    cnt = 0
    while True:
        a = int(x % 2)
        x = int(x/2)
        temp.insert(0, a)
        cnt += 1
        if x <= 0:
            break
    if cnt != n:
        for i in range(n-cnt):
            temp.insert(0, 0)
    return ''.join('#' if i == 1 else ' ' for i in temp)


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = to_binary(i, n)
        b = to_binary(j, n)
        c = ""
        for z in range(len(a)):
            if a[z] == " " and b[z] == " ":
                c += " "
            else:
                c += "#"
        answer.append(c)
    return answer


'''
"asd".zfill(5) = 00asd
"asd".rjust(5,"0")=00asd
bin(10진수)= 0b+2진수 반환
비트 AND& OR| XOR^ NOT~ 가 있다

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
