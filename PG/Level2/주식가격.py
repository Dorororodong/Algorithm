def solution(prices):
    stack = []
    ans = [i for i in range(len(prices) -1, -1, -1)]    # 안 바뀌는 애들은 고대로 (기초세팅)

    for day, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            new_day, _ = stack.pop()
            ans[new_day] = day - new_day
        stack.append((day, price))

    return ans

print(solution([1, 2, 3, 3, 3, 4, 2, 1]))