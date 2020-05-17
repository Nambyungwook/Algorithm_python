n, m = map(int, input().split())

cases = []
ret_set = list(range(n+1))
rank = [0]*(n+1)
ans = []

def find(idx):
    while idx != ret_set[idx]:
        idx = ret_set[idx]
    return idx

def union(a, b):
    #a, b를 입력 받았을 때 a를 기준으로 합한다!
    a = find(a)
    b = find(b)
    if a == b: return

    if rank[a] < rank[b]:
        ret_set[a] = b
        rank[b] += 1
    else:
        ret_set[b] = a
        rank[a] += 1

for i in range(m):
    a,b,c = map(int, input().split())
    cases.append([a,b,c])

for i in range(m):
    if cases[i][0]==0:
        union(cases[i][1], cases[i][2])
    else:
        print("YES" if find(cases[i][1]) == find(cases[i][2]) else "NO")
