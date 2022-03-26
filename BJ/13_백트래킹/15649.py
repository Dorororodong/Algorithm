def perm(l, m, k):
    if m == k:
        print(*result)
        return

    for i in range(1, len(number_list)+1):
        if visited[i] == 0:
            visited[i] = 1
            result.append(l[i-1])
            perm(l, m, k+1)
            visited[i] = 0
            result.pop()

N, M = map(int, input().split())

number_list = [i for i in range(1, N+1)]
visited = [0] * (N + 1)
result = []

perm(number_list, M, 0)