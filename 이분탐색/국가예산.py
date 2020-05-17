def solution(budgets, M):
    mins = 0
    maxs = max(budgets)
    answer = 0

    while mins <= maxs:
        mid = (mins + maxs) // 2

        tmp = []

        for i in budgets:
            if mid>i:
                tmp.append(i)
            else:
                tmp.append(mid)

        if sum(tmp) > M:
            maxs = mid - 1
        elif sum(tmp) <= M:
            answer = mid
            mins = mid + 1

    return answer


budgets = [120, 110, 140, 150]
M = 485
print(solution(budgets, M))