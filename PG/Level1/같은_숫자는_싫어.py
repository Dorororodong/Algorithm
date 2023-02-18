def solution(arr):
    stack = []

    for i in arr:
        if stack:
            if stack[-1] == i:
                continue

            else:
                stack.append(i)

        else:
            stack.append(i)

    return stack

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))