import sys
T = int(sys.stdin.readline().rstrip())

che = [True] * 10001
for i in range(2, 101):
    if che[i]:
        for j in range(2 * i, 10001, i):
            che[j] = False
# print(che)

for _ in range(1, T+1):
    # 4 <= n <= 10000인 짝수
    n = int(sys.stdin.readline().rstrip())
    result = []
    for k in range(2, n // 2 + 1):
        if che[k] == True and che[n-k] == True:
            result.append((k, n - k, abs(2 * k - n)))

    result.sort(key=lambda x: x[2])
    print(result[0][0], result[0][1])

'''
import sys
input = sys.stdin.readline

# 1번 연산_에라토스테네스의 체
A = 10000
dp = [True] * (A + 1)
dp[0] = False
dp[1] = False

for i in range(2, int(A**0.5)+1):
  if dp[i] == True:
    for j in range(i*2, len(dp), i):
      dp[j] = False

# 2번 연산_두 소수의 차이가 가장 작은 경우 찾기 
N = int(input())
for i in range(N):
  B = int(input())
  a = B // 2
  b = a

  while a > 0:
    if dp[a] == True and dp[b] == True:
      print(a, b)
      break
    else:
      a -= 1
      b += 1

# 문제풀이 및 시간 복잡도를 줄이는 방법
1. N+1개의 [True] DP리스트를 만든다.
2. 에라토스테네스의 체는 2중 for문으로 사용하여 해결할 수 있다.
- 첫 번째 for문은 2(변수 i)부터 시작하는 N개까지 움직이는 구조
- 두 번째 for문은 i+i부터 시작해서 N개까지 움직이되 i만큼 움직이는 구조 -> False로 만들어주기
3. 시간 복잡도를 줄이기 위해서 2중 for문은 사실 int(N**0.5 + 1)만큼만 움직이더라도 전부 걸러진다.
4. 두 소수의 차이가 가장 작은 경우를 찾는 것은 사실 두 가지의 경우를 고려해야한다.
- 두 소수의 덧셈이 내가 구하는 값이다. => a + b = 짝수 n(4 ~ 10,000) 

- 두 소수의 차이가 가장 작은게 좋다. => 중간에서부터 1칸씩 멀어지면 된다.
ex) n = 10일 때, 중간을 찾기 위해서 반으로 나눈다. ->  a=5, b=5 
a, b가 둘 다 소수이면 프린트와 break를 통해서 출력과 동시에 연산 중단(두 소수의 차이가 가장 작은 값) 
그렇지 않다면, a는 한 칸 아래쪽으로(-1) b는 한 칸 윗쪽으로(+1) 이동시키고 dp[a]와 dp[b]가 소수인지 확인(무한 루프)
'''