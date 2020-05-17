import sys
from collections import defaultdict

nations = sys.stdin.readline().split()
percentage = defaultdict(int)
expected_score =defaultdict(int)
schedule = []

for _ in range(3):
    tmp = []
    for _ in range(2):
        tmp.append(sys.stdin.readline().split())
    schedule.append(tmp)

def battle(match_day, index, expected_score, rate):
    global total
    global final_score

    #모든매치 종료
    if match_day==3:
        winner = sorted(list(expected_score.items()),key=lambda x: -x[1])

        #전원동점
        if len(set(i[1] for i in winner)) == 1:
            for nation in winner:
                percentage[nation[0]] += rate * (2/len(winner))
            return
        # 2위에서 동점자 존재
        elif winner[0][1] > winner[1][1] and winner[1][1] == winner[2][1]:
            percentage[winner[0][0]] += rate
            equal_value = winner[1][1]
            scores = [i for i in winner if i[1]==equal_value]

            for nation in scores:
                percentage[nation[0]] += rate * (1/len(scores))
            return
        #1위에서 동점자존재
        elif winner[0][1] == winner[1][1]:
            equal_value = winner[0][1]
            scores = [i for i in winner if i[1] == equal_value]
            for nation in scores:
                percentage[nation[0]] += rate * (2/len(scores))
            return
        #동점자 없음
        else:
            for nation in winner[:2]:
                percentage[nation[0]] += rate
            return

    if index == 2:
        battle(match_day + 1, 0, expected_score, rate)
        return

    n1, n2, win, draw, lose = schedule[match_day][index]
    win, draw, lose = map(float, [win, draw, lose])

    #n1>n2
    expected_score[n1] += 3
    battle(match_day, index+1, expected_score, rate*win)
    expected_score[n1] -=3

    #n1=n2
    expected_score[n1] +=1
    expected_score[n2] +=1
    battle(match_day, index+1, expected_score, rate*draw)
    expected_score[n1] -=1
    expected_score[n2] -=1

    #n1<n2
    expected_score[n2] += 3
    battle(match_day, index + 1, expected_score, rate * lose)
    expected_score[n2] -= 3

battle(0,0, expected_score,1)

for nation in nations:
    print(percentage[nation])