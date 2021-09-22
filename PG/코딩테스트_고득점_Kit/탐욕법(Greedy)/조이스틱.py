'''
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동

name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
'''

def solution(name):
    answer = 0
    for i in name:
        if i in ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            answer += (26 + ord('A') - ord(i))
        else:
            answer += (ord(i) - ord('A'))

    # 좌우 순서 찾기

    return answer

print(solution("JEROEN")) # 56
print(solution("JAN"))    # 23