import re

def a(expression, operator):

    copy = expression

    for i in range(0,3):
        offset = 0
        a = operator[i]

        while copy.find(a)!=-1:
            idx = copy.find(a)
            if idx==0:
                offset=1
                idx=copy.find(a,1)
                if idx==-1:
                    break

            frontidx = findNum(copy,idx,True)
            endidx = findNum(copy,idx, False)

            test = re.findall("\d+",copy[idx-frontidx-offset:idx])


            front = int(max(test))
            test_ = re.findall("\d+", copy[idx:idx+endidx+2])
            end = int(test_[0])
            cal = calcul(front, a, end)

            copy = copy.replace(copy[idx-frontidx-offset:idx+endidx+1], str(cal))

    return abs(int(copy))

def findNum(copy, idx, b):
    count = 0
    di=0

    if b:

        di=-1
        while True:
            if idx+di>=0:
                check = copy[idx+di]
                if not check.isdigit():
                    return count
                else:
                    count+=1
                    idx+=di
            else:
                return count

    else:
        di = 1

    while True:
        if idx+di<len(copy):
            check = copy[idx+di]
            if not check.isdigit():
                return count
            else:
                count+=1
                idx+=di
        else:
            return count

def calcul(a, oper, b):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    else:
        return a * b

def solution(expression):
    answer = 0

    # 연산자 우선순위
    cases = [['*', '-', '+'],
             ['*', '+', '-'],
             ['+', '*', '-'],
             ['+', '-', '*'],
             ['-', '*', '+'],
             ['-', '+', '*']]

    res =[]

    for i in range(0,6):
        res.append(a(expression, cases[i]))

    res.sort()

    answer = res[len(res)-1]

    return answer


expression = "100-200*300-500+20"

print(solution(expression))