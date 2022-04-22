import sys
N = int(sys.stdin.readline().rstrip())

dohyun_class = []

for _ in range(N):
    dohyun_class.append(sys.stdin.readline().rstrip().split())

dohyun_class.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in dohyun_class:
    print(i[0])