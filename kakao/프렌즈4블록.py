#i=m, j=n
def solution(m, n, board, number_of_answer):
    # 아래 오른쪽 위
    dx = [1, 1, 0]
    dy = [0, 1, 1]
    answer = {}

    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]==board[i+dx[0]][j+dy[0]] and board[i][j]==board[i+dx[1]][j+dy[1]] and board[i][j]==board[i+dx[2]][j+dy[2]]:
                if answer.get(board[i][j])!=None:
                    tmp = answer[board[i][j]]
                    tmp.extend([[i,j],[i+dx[0],j+dy[0]],[i+dx[1],j+dy[1]],[i+dx[2],j+dy[2]]])
                    answer[board[i][j]] = tmp

                else:
                    answer[board[i][j]] = [[i,j],[i+dx[0],j+dy[0]],[i+dx[1],j+dy[1]],[i+dx[2],j+dy[2]]]

    answer_key_list = list(answer.keys())

    for i in range(len(answer_key_list)):
        tmp_answer = []
        for j in range(len(answer[answer_key_list[i]])):
            tmp_answer.append(str(answer[answer_key_list[i]][j]))

        tmp_answer=list(set(tmp_answer))
        number_of_answer+=len(tmp_answer)

    #보드 없어진 만큼 재조정
    for i in range(len(answer_key_list)):
        tmp_answer = []
        for j in range(len(answer[answer_key_list[i]])):
            tmp_answer.append(str(answer[answer_key_list[i]][j]))

        remove = list(tmp_answer)

    if len(answer)==0:
        return number_of_answer
    else:
        return solution(m,n,board,number_of_answer)


m=4
n=5
board=["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m,n,board,0))
