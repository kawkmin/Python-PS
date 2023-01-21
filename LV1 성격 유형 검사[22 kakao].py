from collections import defaultdict


def solution(survey, choices):
    answer = ""
    dic = defaultdict(int)

    for x, y in zip(survey, choices):
        if y < 4:
            dic[x[0]] += 4 - y
        elif y > 4:
            dic[x[1]] += y % 4

    if dic["R"] > dic["T"]:
        answer += "R"
    elif dic["R"] == dic["T"]:
        answer += min("R", "T")
    else:
        answer += "T"

    if dic["C"] > dic["F"]:
        answer += "C"
    elif dic["C"] == dic["F"]:
        answer += min("C", "F")
    else:
        answer += "F"

    if dic["J"] > dic["M"]:
        answer += "J"
    elif dic["J"] == dic["M"]:
        answer += min("J", "M")
    else:
        answer += "M"

    if dic["A"] > dic["N"]:
        answer += "A"
    elif dic["A"] == dic["N"]:
        answer += min("A", "N")
    else:
        answer += "N"

    return answer


"""
2글자의 조합은 반대인 것만 있는 것을 잘 활용
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
    """
