'''
Finn은 요즘 수학공부에 빠져 있습니다.
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

n은 10,000 이하의 자연수 입니다.
'''

def solution(n):
    cnt = 1
    for i in range(1, n//2 + 1):
        result = i
        for j in range(i+1, n//2 + 2):
            result += j
            if result > n:
                break
            else:
                if result == n:
                    cnt += 1
                    break
    return cnt

print(solution(15))     # 4