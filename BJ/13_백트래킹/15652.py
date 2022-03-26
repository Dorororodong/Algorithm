def perm(l, m, k):
    if m == k:
        print(*result)
        return

    for i in range(1, len(number_list)+1):
        if len(result) == 0:
            result.append(l[i-1])
            perm(l, m, k+1)
            result.pop()
        else:
            if i >= result[-1]:
                result.append(l[i - 1])
                perm(l, m, k + 1)
                result.pop()

N, M = map(int, input().split())

number_list = [i for i in range(1, N+1)]
result = []

perm(number_list, M, 0)