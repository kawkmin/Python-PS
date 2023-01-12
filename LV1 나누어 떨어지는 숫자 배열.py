def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return [-1] if len(answer) == 0 else sorted(answer)


"""
빈 list면 False반환, return A or B 는 둘 중 참인거 반환
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""
