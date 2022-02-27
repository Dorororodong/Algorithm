'''
# index는 그 리스트틑 전부 도는 느낌
list.index(i) 형태의 시간 복잡도 = O(N)

# 그 해당하는 곳만 보니까 1
index[i] 형태의 시간 복잡도 = O(1)
'''

import sys
N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))
idx = sorted(set(X))
dic = {idx[i] : i for i in range(len(idx))}

for i in X:
    print(dic[i], end=' ')

# enumerate : idx, x [앞이 index, 뒤가 값]
'''
import sys
stdin = sys.stdin.buffer

stdin.readline()
arr = list(map(int, stdin.read().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))
'''