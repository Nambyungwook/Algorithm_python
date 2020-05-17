def solution(numbers, hand):
    answer = []
    #숫자별 손가락 위치
    handLocs = {}
    for i in range(10):
        if i==1:
            handLoc = [0,0]
        elif i==2:
            handLoc = [0,1]
        elif i == 3:
            handLoc = [0,2]
        elif i == 4:
            handLoc = [1, 0]
        elif i == 5:
            handLoc = [1, 1]
        elif i == 6:
            handLoc = [1, 2]
        elif i == 7:
            handLoc = [2, 0]
        elif i == 8:
            handLoc = [2, 1]
        elif i == 9:
            handLoc = [2, 2]
        elif i == 0:
            handLoc = [3,1]

        handLocs[i] = handLoc
    #print(handLocs)

    #현재 손가락 위치
    #오른손
    r_loc = [3,2]
    #왼손
    l_loc = [3,0]


    for i in range(len(numbers)):
        answer.append(None)

    for i in range(len(numbers)):
        if numbers[i]==1 or numbers[i] == 4 or numbers[i] == 7:
            answer[i] = 'L'
            l_loc = handLocs[numbers[i]]
        elif numbers[i]==3 or numbers[i] == 6 or numbers[i] == 9:
            answer[i] = 'R'
            r_loc = handLocs[numbers[i]]
        else:
            #가야할 위치
            num_loc = handLocs[numbers[i]]

            #오른손과의 거리
            r_d = abs(num_loc[0]-r_loc[0])+abs(num_loc[1]-r_loc[1])
            #왼손과의 거리
            l_d = abs(num_loc[0]-l_loc[0])+abs(num_loc[1]-l_loc[1])

            if r_d>l_d:
                answer[i]='L'
                l_loc = handLocs[numbers[i]]
            elif l_d>r_d:
                answer[i]='R'
                r_loc = handLocs[numbers[i]]
            else:
                if hand == "right":
                    answer[i]='R'
                    r_loc = handLocs[numbers[i]]
                elif hand == "left":
                    answer[i]='L'
                    l_loc = handLocs[numbers[i]]
    ret = [""]
    for i in range(len(answer)):
        ret[0] += answer[i]

    return ret[0]


number = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(number, hand))