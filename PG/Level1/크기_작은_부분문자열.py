def solution(t, p):
    n1 = len(t)
    n2 = len(p)
    cnt = 0

    for i in range(n1 - n2 + 1):
        if t[i:i+n2] <= p:
            cnt += 1

    return cnt

print(solution("3141592", "271"))


'''
int로 변환하면 더 걸림, 근데 int로 안해줘도 알아서 대소비교 가능?!
'''