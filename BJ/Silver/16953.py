opr = [2, 1]
def DFS(s, f, n):
    global min_result

    if s > f:
        return

    if s == f:
        if min_result > n:
            min_result = n
            return

    for i in opr:
        if i == 2:
            DFS(s * 2, f, n+1)
        else:
            DFS(s * 10 + 1, f, n+1)

A, B = map(int, input().split())

min_result = 987654321

DFS(A, B, 1)

if min_result == 987654321:
    min_result = -1

print(min_result)


'''
BFS
'''

'''
반복문
'''