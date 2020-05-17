M = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []


N = int(input())

#방문확인
vst = []

for i in range(N):
    M.append(list(input()))

vst = [[0 for col in range(N)] for row in range(N)]

for i in range(N):
    for j in range(N):
        if M[i][j] == "1":
            vst[i][j] = "N"

def bfs(i, j, vst):
    queue = [[i, j]]
    vst[i][j] = 'N'
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < N and 0 <= y < N and M[x][y] == "1" and vst[x][y] == 'N':
                vst[x][y] = "V"
                queue.append([x, y])
                count += 1
    cnt.append(count)

for i in range(N):
    for j in range(N):
        if M[i][j] == '1':
            bfs(i,j,vst)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])