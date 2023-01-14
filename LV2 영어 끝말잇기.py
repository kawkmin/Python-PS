from collections import defaultdict


def solution(n, words):
    d = defaultdict(int)

    for i, x in enumerate(words):
        d[x] += 1
        if d[x] == 2 or i >= 1 and words[i - 1][-1] != x[0]:
            return [i % n + 1, i // n + 1]

    return [0, 0]


"""
in을 왜 자꾸 까먹지..
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: 
            return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
"""
