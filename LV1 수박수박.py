def solution(n):
    return "".join(["수" if i % 2 == 0 else "박" for i in range(n)])


"""
def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])
"""
