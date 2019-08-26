N = int(input())
cnt = 0

def hanoi(N, a, b, c):
    if N==1:
        print(a, c)
        return None
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)


for i in range(0, N):
    cnt = 2*cnt + 1
print(cnt)
hanoi(N, 1, 2, 3)