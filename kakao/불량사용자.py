from copy import deepcopy
import re

# 해당 조합의 중복여부를 확인하기 위한 리스트
check = []


def dfs_check(idx, candidates, arr, length):
    global answer, check
    # 조합 끝까지 전부 확인한 경우
    if idx == len(candidates):
        # banned_id 길이와 일치하고, 중복된 조합이 아닐 경우
        if len(arr) == length and arr not in check:
            # 조합 리스트에 저장
            check.append(deepcopy(arr))
        return

    # 각 banned_id 패턴별로 가능한 경우의 수를 토대로 조합을 만든다
    for each_id in candidates[idx]:
        # 만약 조합에 id가 없을 경우
        if each_id not in arr:
            # 조합에 저장
            arr.add(each_id)
            dfs_check(idx + 1, candidates, arr, length)
            # 백트래킹
            arr.remove(each_id)


def solution(user_id, banned_id):
    candidates = []

    for i in range(len(banned_id)):
        # banned id여부를 체크할 정규식을 만든다.
        banned_id[i] = re.compile("^" + banned_id[i].replace("*", "([0-9]|[a-z])") + "$")
        temp = set()
        # 해당 정규식으로 매칭할 수 있는 user id를 저장한다.
        for each_user in user_id:
            if banned_id[i].match(each_user):
                temp.add(each_user)

        # 각 banned_id 패턴에 부합하는 user id 조합을 저장한다.
        candidates.append(temp)

    dfs_check(0, candidates, set(), len(banned_id))
    return len(check)


print(solution(user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]	, banned_id=["*rodo", "*rodo", "******"]	))