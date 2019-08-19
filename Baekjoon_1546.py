N = int(input())
score = list(map(int, input().split()))

score.sort()

newScore = []

highScore = score[N-1]

sum = 0

for i in range(0, N):
    newScore.append(score[i]/highScore*100)

for i in range(0, N):
    sum += newScore[i]

print(sum/N)