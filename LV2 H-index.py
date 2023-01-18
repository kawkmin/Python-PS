def solution(numbers, hand):
    answer = ""
    L_loc = 10
    R_loc = 12
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            L_loc = i

        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            R_loc = i
        else:
            if i == 0:
                i = 11
            a = abs(i - L_loc)
            b = abs(i - R_loc)
            x = (a // 3) + (a % 3)  # 이부분 못했음
            y = (b // 3) + (b % 3)
            if x > y:
                answer += "R"
                R_loc = i
            elif x < y:
                answer += "L"
                L_loc = i
            else:
                if hand == "right":
                    answer += "R"
                    R_loc = i
                else:
                    answer += "L"
                    L_loc = i

    return answer


def solution(citations):
    for i, x in enumerate(sorted(citations)):
        if x >= len(citations) - i:
            return len(citations) - i
    return 0
