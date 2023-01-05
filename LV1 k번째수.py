def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer


'''
def solution(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
'''
