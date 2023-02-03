def solution(s, skip, index):
    answer = ""
    for c in s:
        c = ord(c)
        for i in range(1, index + 1):
            c += 1
            if c > ord("z"):
                c = ord("a")
            if chr(c) in skip:
                while chr(c) in skip:
                    c += 1
                    if c > ord("z"):
                        c = ord("a")
        answer += chr(c)
    return answer


"""
set으로도 사용 가능
def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    for i in s:
        answer += arr[(arr.index(i) + index)%len(arr)]
    return answer
"""
