def solution(d, budget):
    d.sort()                # O(nlogn)
    total = sum(d)          # O(n)
    n = len(d)

    if total <= budget:
        return n

    else:
        for i in range(n - 1, 0, -1):        # O(n)
            if total - d[i] <= budget:
                return i

            else:
                total -= d[i]

        return 0

print(solution([1, 3, 2, 5, 4], 9))