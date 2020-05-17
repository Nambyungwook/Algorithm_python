import copy


def multiply(arr):
    ret = 1
    for n in arr:
        if int(n) == 0:
            return 0
        ret *= int(n)
    return ret

def minus(arr):
    ret = int(arr[0])*2
    for n in arr:
        ret -= int(n)
    return ret

def plus(arr):
    ret=0
    for n in arr:
        ret += int(n)
    return ret



def solution(expression):

    #연산자 우선순위
    cases = [['*','+','-'],
             ['*','-','+'],
             ['+','*','-'],
             ['+','-','*'],
             ['-','*','+'],
             ['-','+','*']]
    answer = []



    for i in range(len(cases)):
        tmp_ex = copy.copy(expression)
        for j in range(len(expression)):
            if expression[j]==cases[i][0]:
                tmp = expression[j-3:j+4]



                test = eval(tmp)
                tmp_ex.replace(expression[j-3:j+4],str(test),1)

                answer.append(tmp_ex)

    return answer

expression="100-200*300-500+20"

print(solution(expression))


expression.isdigit()
