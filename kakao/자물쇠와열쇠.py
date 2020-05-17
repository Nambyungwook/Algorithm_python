#오른쪽 90도 회전 -> 4번하면 360도
import copy


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def rotateN(m, n):
    ret = []

    if n==0:
        ret = m
    elif n==1:
        ret = rotate_90(m)
    elif n==2:
        ret = rotate_90(rotate_90(m))
    elif n==3:
        ret = rotate_90(rotate_90(rotate_90(m)))

    return ret

def solution(key, lock):

    real_answer = False
    except_cases = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            except_cases.append(lock[i][j])
    if except_cases.count(1)==len(lock)*len(lock):
        real_answer = True
        return real_answer

    T = len(key)+len(key)+len(lock)-2#큰배열크기
    #lock배열의 위치=> (len(key)-1,len(key)-1) ~ (len(key)-1+len(lock)-1,len(key)-1+len(lock)-1)
    lock_i = len(key)-1

    BIG_MATRIX = [[0 for col in range(T)] for row in range(T)]

    for i in range(len(lock)):
        for j in range(len(lock)):
            BIG_MATRIX[len(key)-1+i][len(key)-1+j] = lock[i][j]



    for i in range(4):
        tmp_key = rotateN(key, i)
        res = copy.deepcopy(BIG_MATRIX)

        for p in range(len(lock)+len(tmp_key)-1):
            for q in range(len(lock)+len(tmp_key)-1):

                answer = []
                for j in range(len(tmp_key)):
                    for k in range(len(tmp_key)):

                        res[p+j][q+k]=BIG_MATRIX[p+j][q+k]+tmp_key[j][k]

                # for j in range(len(res)):
                #     print(res[j])
                # print('----------------------')

                for i in range(len(lock)):
                    for j in range(len(lock)):
                        answer.append(res[len(key) - 1 + i][len(key) - 1 + j])

                if answer.count(1) == len(lock) * len(lock):
                    real_answer = True

                res = copy.deepcopy(BIG_MATRIX)



    if real_answer==True:
        return real_answer
    else:
        return real_answer

key = [[0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0],[0,0,0,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
#lock = [[1,1,1],[1,1,1],[1,1,1]]
print(solution(key, lock))



