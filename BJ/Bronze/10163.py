import sys
N = int(sys.stdin.readline().rstrip())

if N == 1:
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a * b)

else:
    arr = [[0] * 1001 for _ in range(1001)]

    for i in range(1, N + 1):
        x, y, a, b = map(int, sys.stdin.readline().rstrip().split())

        for j in range(y, y+b):
            arr[j][x:x+a] = [i] * a     # 뭉텅이로 바꿔주는 부분! (하나씩이 아니라...)

    for k in range(1, N + 1):
        ans = 0
        for n in range(1001):
            ans += arr[n].count(k)

        print(ans)

'''
# idx 시도 해봤었는데... 이렇게 하는 거였구만...
def get_surface_area(points):
    ans = [0] * T
    
    for idx, point in enumerate(points):
        for i in range(point[0], point[0]+point[2]):
            for j in range(point[1], point[1]+point[3]):
                matrix[i][j] = idx+1
    
    for m in range(1001):
        for n in range(1001):
            if matrix[m][n]:
                x = matrix[m][n]
                ans[x-1] += 1
    return ans
    
    
T = int(input())
points = [list(map(int, input().split())) for _ in range(T)]
matrix = [[0]*1001 for _ in range(1001)]

results = get_surface_area(points)
for result in results:
    print(result)
'''