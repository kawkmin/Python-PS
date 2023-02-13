def solution(checklist):
    checklist = sorted(checklist, key=lambda x: x[-1])
    cnt = 0
    temp = -30001

    for i in range(len(checklist)):
        if temp < checklist[i][0]:
            cnt += 1
            temp = checklist[i][1]

    return cnt
