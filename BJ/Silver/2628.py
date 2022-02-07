import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
width = [0]
length = [0]
T = int(sys.stdin.readline().rstrip())
for _ in range(1, T+1):
    d, x = map(int, sys.stdin.readline().rstrip().split())

    if d == 1:
        width.append(x)

    else:
        length.append(x)

width += [N]
length += [M]

width.sort()
length.sort()

result_width = []
result_length = []

for i in range(len(width)-1):
    result_width.append(width[i+1] - width[i])

for j in range(len(length)-1):
    result_length.append(length[j+1] - length[j])

print(max(result_width) * max(result_length))