cnt = 0

def solution(numbers, target):
    n = len(numbers)

    def dfs(idx, res):
        if idx == n:
            if res == target:
                global cnt
                cnt += 1
            return
        else:
            dfs(idx + 1, res + numbers[idx])
            dfs(idx + 1, res - numbers[idx])

    dfs(0, 0)
    return cnt


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))


def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(idx, res):
        if idx == n:
            if res == target:
                nonlocal cnt
                cnt += 1
            return
        else:
            dfs(idx + 1, res + numbers[idx])
            dfs(idx + 1, res - numbers[idx])

    dfs(0, 0)
    return cnt