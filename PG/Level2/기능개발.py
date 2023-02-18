def solution(progresses, speeds):
    stack = []
    ans = []
    n = len(progresses)

    for i in range(n):
        if (100-progresses[i]) % speeds[i]:
            stack.append((100-progresses[i]) // speeds[i] + 1)

        else:
            stack.append((100 - progresses[i]) // speeds[i])

    for i in range(n-1):
        if stack[i] > stack[i+1]:
            stack[i+1] = stack[i]

    ans.append(1)
    for i in range(1, n):
        if stack[i-1] == stack[i]:
            ans[-1] += 1

        else:
            ans.append(1)

    return ans

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))