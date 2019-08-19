N = []
num = []
aws = [0]*42
cnt = 0

for i in range(0, 10):
    tmp = int(input())
    N.append(tmp)

for i in range(0, 10):
    tmp = N[i]%42
    num.append(tmp)

for i in range(0, 10):
    aws[num[i]] += 1

for i in range(0, 42):
    if aws[i]!=0:
        cnt +=1

print(cnt)