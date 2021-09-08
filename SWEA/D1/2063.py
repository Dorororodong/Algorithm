N = int(input())

score = list(map(int, input().split()))

print(sorted(score)[N//2])