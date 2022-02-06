import sys
T = int(sys.stdin.readline().rstrip())

drawing_paper = [[0] * 100 for _ in range(100)]

for _ in range(1, T+1):
    y, x = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if drawing_paper[i][j] == 0:
                drawing_paper[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if drawing_paper[i][j] == 1:
            cnt += 1

print(cnt)