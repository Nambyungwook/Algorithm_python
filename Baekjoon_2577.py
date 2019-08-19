A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)
N = []
ret = [0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(num)):
    tmp = int(num[i])
    N.append(tmp)

for i in range(0, len(N)):
    if N[i]==0:
        ret[0] += 1
    elif N[i]==1:
        ret[1] += 1
    elif N[i]==2:
        ret[2] += 1
    elif N[i]==3:
        ret[3] += 1
    elif N[i]==4:
        ret[4] += 1
    elif N[i]==5:
        ret[5] += 1
    elif N[i]==6:
        ret[6] += 1
    elif N[i]==7:
        ret[7] += 1
    elif N[i]==8:
        ret[8] += 1
    elif N[i]==9:
        ret[9] += 1

for i in range(0,10):
    print(ret[i])
