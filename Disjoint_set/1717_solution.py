import sys
input = sys.stdin.readline

class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n

    def find(self, idx):
        while idx != self.parent[idx]:
            idx = self.parent[idx]
        return idx

    def union(self, a, b):
        #a, b를 입력 받았을 때 a를 기준으로 합한다!
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
            self.rank[b] += 1
        else:
            self.parent[b] = a
            self.rank[a] += 1


n, m = map(int, input().split())
obj = DisjointSet(n + 1)
for _ in range(m):
    f, a, b = map(int, input().split())
    if f:
        #a와 b가 같은 집합인지 확인.
        print("YES" if obj.find(a) == obj.find(b) else "NO")
    else:
        #a와 b를 합
        obj.union(a, b)