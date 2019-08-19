C = int(input())
Score = []
overAVGRatio = []

for i in range(0, C):
    tmpScore = list(map(int, input().split()))
    N = tmpScore[0]
    for j in range(1, N+1):
        Score.append(tmpScore[j])
    avg = sum(Score)/N
    tmpScore.clear()
    cnt = 0
    for j in range(0, N):
        if Score[j]>avg:
            cnt += 1
    Score.clear()

    tmpRatio = float(100*(cnt/N))
    overAVGRatio.append(round(tmpRatio,3))

for i in range(0, C):
    print("%.3f%%" %overAVGRatio[i])