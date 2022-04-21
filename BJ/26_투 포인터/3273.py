import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

arr.sort()
cnt = 0
left = 0
right = n - 1

while left < right:
    if arr[left] + arr[right] < x:
        left += 1

    elif arr[left] + arr[right] == x:
        cnt += 1
        right -= 1

    else:
        right -= 1

print(cnt)