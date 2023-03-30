from collections import Counter


def solution(k, tangerine):
    answer = 0
    for i in sorted(Counter(tangerine).items(), key=lambda x: -x[1]):
        answer += 1
        if k <= i[1]:
            return answer
        else:
            k -= i[1]
