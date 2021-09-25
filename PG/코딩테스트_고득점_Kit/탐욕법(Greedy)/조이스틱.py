'''
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동

name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
'''

def solution(name):
    joystick = []
    for i in name:  # 최소 거리 저장 (아스키 코드 / 좌우 그 중간 지점이 있음 90~65)
        joystick.append(min(ord(i) - ord('A'), ord('Z') - ord(i) + 1))
    
    # print(joystick)
    
    i, answer = 0, 0
    while True:                     # 좌우 탐색 확인
        answer += joystick[i] 
        joystick[i] = 0             # 더해주면 0으로 제거
        
        if sum(joystick) == 0:      # 완료되면 출력
            return answer
        
        left, right = 1, 1          # 좌우 탐색
        
        while joystick[i - left] == 0:  # 좌는 인덱스 감소 ('A'가 나오면!)
            left += 1

        while joystick[i + right] == 0: # 우는 인덱스 증가 ('A'가 나오면!)
            right += 1
        
        if right > left:                # 'A'가 나온게 우측이면
            answer += left              # 왼쪽으로 진행하는게 이득
            i -= left                   # 왼쪽으로 계속 진행
        else:                           # 반대!
            answer += right
            i += right

print(solution("JEROEN"))           # 56
print(solution("JAN"))              # 23
print(solution("BBABAAAB"))         # 11
print(solution("AAAA"))             # 0
print(solution("ABBAAAAAAAAAB"))    # 8
