N =  int(input())
tmp = set()


for i in range(1, N+1):
    if i<10:
        tmp.add(i)
    elif 10<=i<100:
        tmp.add(i)
    elif 100<=i<1000:
        A = int(i/100)
        B = int((i-100*A)/10)
        C = i%10
        if B-A == C-B:
            tmp.add(i)

print(len(tmp))