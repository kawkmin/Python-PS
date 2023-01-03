def solution(s):
    m = {}
    for i in s.lower():
        m[i]=m.get(i,0)+1

    if m.get('p',0)==m.get('y',0):
        return True

    return False

'''
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
'''