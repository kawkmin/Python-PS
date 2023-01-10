def solution(N, stages):
    answer = []
    d1 = {}
    d2 = {}
    for i in stages:
        d1[i] = d1.get(i, 0)+1

    for i in range(1, N+1):
        s_sum = len(stages)

        for j in range(1, i):
            s_sum -= d1.get(j, 0)

        if s_sum == 0:
            d2[i] = 1
            continue
        d2[i] = (s_sum - d1.get(i, 0))/s_sum

    return sorted(d2, key=lambda x: d2[x])


'''
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''
