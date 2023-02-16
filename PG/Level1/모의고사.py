def solution(answers):
    no1 = [1, 2, 3, 4, 5]
    no2 = [2, 1, 2, 3, 2, 4, 2, 5]
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    win = []
    n = len(answers)

    for i in range(n):
        if answers[i] == no1[i % 5]:
            ans[0] += 1

        if answers[i] == no2[i % 8]:
            ans[1] += 1

        if answers[i] == no3[i % 10]:
            ans[2] += 1

    cnt = max(ans)

    for i in range(3):
        if ans[i] == cnt:
            win.append(i + 1)

    return win

print(solution([1,3,2,4,2]))

'''
enumerate() = idx, val
'''