def solution(sizes):
    max_size = []
    min_size = []

    for i in sizes:                 # O(n)
        if i[0] >= i[-1]:
            max_size.append(i[0])
            min_size.append(i[-1])

        else:
            max_size.append(i[-1])
            min_size.append(i[0])

    max_size.sort()
    min_size.sort()

    return max_size[-1] * min_size[-1]

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))