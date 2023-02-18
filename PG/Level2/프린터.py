from collections import deque

def solution(priorities, location):
    d_priorities = deque(enumerate(priorities))
    ans = 0

    while d_priorities:
        idx, val = d_priorities.popleft()
        n = len(d_priorities)

        if n and max(d_priorities, key=lambda x : x[1])[1] > val:
            d_priorities.append((idx, val))

        else:
            ans += 1
            if idx == location:
                break
    return ans

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))