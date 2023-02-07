def solution(genres, plays):
    answer = []
    dic = {}
    li = []

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        li.append([i, genres[i], plays[i]])

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    li.sort(key=lambda x: x[2], reverse=True)
    for x in dic:
        print(x)
        cnt = 0
        for y in li:
            if cnt == 2:
                break
            if y[1] == x[0]:
                cnt += 1
                answer.append(y[0])

    return answer
