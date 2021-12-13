'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
'''

def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue

        if ord(i) <= 90:
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)

        elif ord(i) <= 122:
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)

    return answer

print(solution("AB", 1))        # "BC"
print(solution("z", 1))         # "a"
print(solution("a B z", 4))     # "e F d"
