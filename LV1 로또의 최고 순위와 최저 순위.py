def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    sum1 = 0
    sum2 = 0
    for i in lottos:
        if i == 0:
            sum1 += 1

    for i in win_nums:
        if i in lottos:
            sum2 += 1
    sum1 += sum2

    return [rank[sum1], rank[sum2]]


'''
잘 했는데, count를 또 까먹음..
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''
