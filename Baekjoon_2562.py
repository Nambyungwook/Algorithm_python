num = []
max = 0
index = 0

for i in range(0,9):
    tmp = int(input())
    num.append(tmp)

for i in range(0,9):
    if(num[i]>=max):
        max = num[i]
        index = i+1


print(max)
print(index)
