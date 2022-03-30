import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))

    elif n == 2:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        print(max(sticker[0][1], sticker[1][1]))

    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        for i in range(2, n):
            sticker[0][i] += max(sticker[1][i-2], sticker[1][i-1])
            sticker[1][i] += max(sticker[0][i-2], sticker[0][i-1])

        print(max(sticker[0][n-1], sticker[1][n-1]))

'''
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    up=list(map(int,input().split()))
    down=list(map(int,input().split()))
  
    if n>1:
        up[1]+=down[0]
        down[1]+=up[0]
        
        for i in range(2,n):
            up[i]+=max(down[i-1], down[i-2])
            down[i]+=max(up[i-1], up[i-2])

    print(max(up[-1],down[-1]))
'''