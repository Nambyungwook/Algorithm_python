def solution2(board, moves, basket, cnt):
    # i의 최대
    max_depth = len(board)

    for i in range(max_depth):
        if board[i][moves[0] - 1] != 0:
            basket.append(board[i][moves[0] - 1])
            board[i][moves[0] - 1] = 0

            if len(basket) > 1:
                if basket[len(basket) - 1] == basket[len(basket) - 2]:
                    basket.pop(len(basket) - 1)
                    basket.pop(len(basket) - 1)
                    cnt += 2

            moves.pop(0)
            if len(moves) != 0:
                return solution2(board, moves, basket, cnt)
            else:
                anwser = cnt

                return anwser
        elif i == max_depth - 1:
            moves.pop(0)
            if len(moves) != 0:
                return solution2(board, moves, basket, cnt)
            else:
                anwser = cnt

                return anwser


def solution(board, moves):
    basket = []
    cnt = 0
    board = board
    moves = moves

    return solution2(board, moves, basket, cnt)

