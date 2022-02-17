import sys
N = int(sys.stdin.readline().rstrip())
cute = 0
no_cute = 0

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 1:
        cute += 1

    else:
        no_cute += 1

if cute > no_cute:
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')