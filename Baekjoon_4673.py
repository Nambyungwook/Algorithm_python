U = set()
tmp = set()
res = []

for i in range(0, 10000):
    U.add(i)

for i in range(0, 10):
    for j in range(0, 10):
        if 11*i+2*j<100:
            tmp.add(11*i+2*j)
        for k in range(0, 10):
            if 100<=101*i+11*j+2*k<1000:
                tmp.add(101*i+11*j+2*k)
            for t in range(0, 10):
                if 1000<=1001*i+101*j+11*k+2*t<10000:
                    tmp.add(1001*i+101*j+11*k+2*t)
result=U-tmp
for i in range(0, len(result)):
    res.append(result.pop())

res.sort()
for i in  range(0, len(res)):
    print(res[i])