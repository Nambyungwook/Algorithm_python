def check(stones, k, mid):
    now = 0
    for stone in stones:
        if (stone < mid):
            now += 1

        else:
            now = 0
        if (now >= k):
            return False
    return True


def solution(stones, k):
    left = 1
    right = max(stones) + 1
    while (left < right - 1):
        mid = (left + right) // 2
        if (check(stones, k, mid)):
            left = mid
        else:
            right = mid

    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

k = 3

print(solution(stones, k))