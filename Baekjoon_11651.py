N = int(input())

location = []

for i in range(0, N):
    x, y = map(int, input().split())
    location.append([x, y])

sortedLocation = sorted(location, key=lambda x:(x[1], x[0]))

for i in range(0, N):
    print(sortedLocation[i][0], sortedLocation[i][1])