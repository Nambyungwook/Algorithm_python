def solution(baseball):
    answer = []

    for i in range(123, 988):
        answer.append(i)

    return solution2(baseball, answer)


def solution2(baseball, answer):
    answer_ = []

    for j in answer:
        j_num = str(j)
        case_num = str(baseball[0][0])
        case_strike_num = baseball[0][1]
        case_ball_num = baseball[0][2]

        tmp_strike = 0
        tmp_ball = 0

        if not (j_num[0] == j_num[1] or j_num[0] == j_num[2] or j_num[1] == j_num[2]):
            if j_num == case_num:
                tmp_strike = 3
            else:
                if (j_num[0] == case_num[0] and j_num[1] == case_num[1]) or (
                        j_num[0] == case_num[0] and j_num[2] == case_num[2]) or (
                        j_num[2] == case_num[2] and j_num[1] == case_num[1]):
                    tmp_strike = 2
                else:
                    if j_num[0] == case_num[0]:
                        tmp_strike = 1

                        if j_num[1] == case_num[2] and j_num[2] == case_num[1]:
                            tmp_ball = 2
                        elif j_num[1] == case_num[2]:
                            tmp_ball = 1
                        elif j_num[2] == case_num[1]:
                            tmp_ball = 1
                        else:
                            tmp_ball = 0

                    elif j_num[1] == case_num[1]:
                        tmp_strike = 1

                        if j_num[0] == case_num[2] and j_num[2] == case_num[0]:
                            tmp_ball = 2
                        elif j_num[0] == case_num[2]:
                            tmp_ball = 1
                        elif j_num[2] == case_num[0]:
                            tmp_ball = 1
                        else:
                            tmp_ball = 0

                    elif j_num[2] == case_num[2]:
                        tmp_strike = 1

                        if j_num[0] == case_num[1] and j_num[1] == case_num[0]:
                            tmp_ball = 2
                        elif j_num[0] == case_num[1]:
                            tmp_ball = 1
                        elif j_num[1] == case_num[0]:
                            tmp_ball = 1
                        else:
                            tmp_ball = 0

                    else:
                        tmp_strike = 0
                        for i in range(len(j_num)):
                            for k in range(len(case_num)):
                                if j_num[i] == case_num[k] and i != k:
                                    tmp_ball += 1

        if tmp_strike == case_strike_num and tmp_ball == case_ball_num:
            if j_num[0] == '0' or j_num[1] == '0' or j_num[2] == '0':
                continue
            else:
                tmp_num = int(j_num)
                answer_.append(tmp_num)

    baseball = baseball[1:]

    if len(baseball) == 0:
        return len(answer_)
    else:
        return solution2(baseball, answer_)

