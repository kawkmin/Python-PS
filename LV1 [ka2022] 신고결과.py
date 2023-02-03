from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    dic = {}
    visit = defaultdict(set)
    for rep in set(report):
        a, b = rep.split()
        visit[a].add(b)
        dic[b] = dic.get(b, 0) + 1

    for i in id_list:
        result = 0
        for x in visit[i]:
            if dic[x] >= k:
                result += 1
        answer.append(result)

    return answer


"""
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
"""
