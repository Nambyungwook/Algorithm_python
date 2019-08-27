a=[]
b=[]
c=[]

checker = True

result = []

while(checker):
    a_tmp, b_tmp, c_tmp = map(int, input().split())
    if a_tmp==0:
        checker = False
    else:
        a.append(a_tmp)
        b.append(b_tmp)
        c.append(c_tmp)

for i in range(0, len(a)):
    tri_tmp = []
    tri_tmp.append(int(a[i]))
    tri_tmp.append(int(b[i]))
    tri_tmp.append(int(c[i]))

    tri_tmp.sort()

    A = tri_tmp[0]*tri_tmp[0]
    B = tri_tmp[1]*tri_tmp[1]
    C = tri_tmp[2]*tri_tmp[2]

    if C == (A+B):
        result.append("right")
        tri_tmp.clear()
    else:
        result.append("wrong")
        tri_tmp.clear()

for i in range(0, len(result)):
    print(result[i])