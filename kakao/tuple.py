import re

def solution(s):
    #가장자리 {}삭제
    s = s[1:len(s)-1]
    #집합원소수
    cases_num=s.count('{')

    set_numbers = []

    for i in range(len(s)):
        if s[i]=='{':
            cnt = 0
            j=i+1
            while True:
                if s[j]!='}':
                    cnt+=1
                    j+=1
                elif s[j]=='}':
                    break

            numbers=re.findall('\d+', s[i:i+cnt+1])
            set_numbers.append(numbers)

    #원소수 배열
    tmp_num = []
    #임시
    tmp_set_numbers = []
    for i in range(cases_num):
        tmp_num.append(len(set_numbers[i]))

    tmp_num.sort()
    for i in range(cases_num):
        for j in range(cases_num):
            if tmp_num[i]==len(set_numbers[j]):
                tmp_set_numbers.append(set_numbers[j])

    set_numbers = tmp_set_numbers

    #답
    real_answer = []
    answer = []
    for i in range(cases_num):
        #원소의 원소수
        j = len(set_numbers[i])
        if j==1:
            answer.append(set_numbers[i][0])
        else:
            for k in range(j):
                if answer.count(set_numbers[i][k])==0:
                    answer.append(set_numbers[i][k])

    for i in range(len(answer)):
        temp = answer[i]
        real_answer.append(int(temp))


    return real_answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))