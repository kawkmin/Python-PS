def solution(board, moves):
    answer = 0
    basket = [0]
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                temp = board[i][move - 1]
                board[i][move - 1] = 0
                if basket[-1] == temp:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(temp)
                break

    return answer
