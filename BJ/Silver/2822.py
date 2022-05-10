import sys
res = []
for i in range(1, 9):
    res.append((i, int(sys.stdin.readline().rstrip())))

res.sort(key=lambda x : x[1], reverse=True)

ans = 0
ans_list = []
for j in range(5):
    ans += res[j][1]
    ans_list.append(res[j][0])

ans_list.sort()

print(ans)
print(' '.join(map(str, ans_list)))