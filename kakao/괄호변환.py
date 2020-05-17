# 2. 문자열 w를 균형잡힌 괄호 문자열로 구분하는 함수.
# 균형잡힌 괄호 문자열이 만들어지는 index를 반환한다.
def balanced(p):
    num = 0
    temp = []
    for idx, value in enumerate(p):
        if value == ")":
            num -=1
        if value == "(":
            num +=1
        if num == 0:
            return idx

# 3. 올바른 괄호 문자열인지 확인하는 함수
def is_right(string):
    temp = []
    for i in string:
        if i == "(":
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    if len(temp) != 0:
        return False
    return True

def solution(p):
    # 1. 빈 문자열이거나 문자열 전체가 올바른 괄호 문자열.. 그대로 반환한다.
    if p == "" or is_right(p): return p
    # 2. 문자열 w를 균형잡힌 괄호 문자열로 분리한다.
    u, v = p[:balanced(p)+1], p[balanced(p)+1:]
    # 3. 문자열 u가 올바른 괄호 문자열일 경우
    if is_right(u):
        # 3. 문자열 v를 1단계부터 수행
        string = solution(v)
        # 수행한 결과를 u에 이어붙여 반환한다.
        return u + string
    # 4. 올바른 괄호 문자열이 아닌 경우
    else:
        # 4.1 첫 번째 문자열 (
        t = "("
        # 4.2 v를 재귀적으로 수행한 결과를 이어붙인다
        t += solution(v)
        # 4.3
        t += ")"
        # 4.4 u의 맨 앞과 뒷문자 제거하고,
        u = list(u[1:-1])
        # 나머지 문자열의 괄호 방향을 뒤집는다.
        for i in range(len(u)):
            if u[i] == '(': 
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
        t += "".join(u)
        # 생성된 문자열을 반환한다.
        return t

p = "(()())()"

print(solution(p))