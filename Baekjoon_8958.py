N = int(input())
oxStr = []
tmpScore = []
Score = []

for i in range(0, N):
    tmp = input()
    oxStr.append(tmp)
    for j in range(0, len(oxStr[i])):
        tmpOXStr = oxStr[i]
        if tmpOXStr[j] == 'O':
            if j!=0 and tmpOXStr[j-1]=='O':
                tmpScore.append(tmpScore[j-1] + 1)
            else:
                tmpScore.append(1)
        else:
            tmpScore.append(0)

    Score.append(sum(tmpScore))
    tmpScore.clear()

for i in range(0,N):
    print(Score[i])