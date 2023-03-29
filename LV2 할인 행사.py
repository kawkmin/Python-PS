from collections import defaultdict


def solution(want, number, discount):
    answer = 0

    wan_dic = defaultdict(int)
    for i in range(len(number)):
        wan_dic[want[i]] += number[i]

    dic = defaultdict(int)
    for i in range(len(discount) - 9):

        if i == 0:
            for j in range(i, i + 10):
                dic[discount[j]] += 1
        else:
            dic[discount[i - 1]] -= 1
            dic[discount[i + 9]] += 1

        if possible(wan_dic, dic):
            answer += 1

    return answer


def possible(wan_dic, dic):
    for i in wan_dic.items():
        if i[1] > dic[i[0]]:
            return False
    return True


# from collections import Counter
# def solution(want, number, discount):
#     answer = 0
#     dic = {}
#     for i in range(len(want)):
#         dic[want[i]] = number[i]

#     for i in range(len(discount)-9):
#         if dic == Counter(discount[i:i+10]):
#             answer += 1

#     return answer
