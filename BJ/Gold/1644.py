# 소수 거르는 로직... int(ath.sqrt(N)) + 1을 사용해도 시간이 더 줄 것 같기도 하고...

import sys
N = int(sys.stdin.readline().rstrip())
Eratosthenes = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if Eratosthenes[i]:
        primes.append(i)

        for j in range(2 * i, N + 1, i):
            Eratosthenes[j] = False

cnt = 0
res = 0
left = right = 0        # 투 포인터!!!

for right in range(len(primes)):
    res += primes[right]

    while res >= N:
        if res == N:
            cnt += 1
        res -= primes[left]
        left += 1

print(cnt)

'''
# 개오래 걸림! (통과는 함...)
import sys
N = int(sys.stdin.readline().rstrip())
Eratosthenes = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if Eratosthenes[i]:
        primes.append(i)

        for j in range(2 * i, N + 1, i):
            Eratosthenes[j] = False

cnt = 0

for i in range(len(primes)):
    if primes[i] > N:
        break

    elif primes[i] == N:
        cnt += 1

    else:
        if i == len(primes) - 1:
            break

        else:
            for j in range(i + 1, len(primes)):
                if N == sum(primes[i : j]):
                    cnt += 1
                    break

                if N < sum(primes[i : j]):
                    break

print(cnt)
'''