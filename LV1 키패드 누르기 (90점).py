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
            x = (a // 3) + (a % 3)  # 이부분 못했음 3이상의 차이= 1의 차이
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


"""
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
"""
