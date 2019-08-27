x=[]
y=[]

for i in range(0, 3):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)

if x[0]==x[1]:
    X=x[2]
elif x[0]==x[2]:
    X=x[1]
else:
    X=x[0]

if y[0]==y[1]:
    Y=y[2]
elif y[0]==y[2]:
    Y=y[1]
else:
    Y=y[0]

print(X, Y)