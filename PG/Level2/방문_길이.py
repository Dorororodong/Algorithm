'''
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다.
명령어는 다음과 같습니다.
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

명령어가 매개변수 dirs로 주어질 때,
게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
dirs의 길이는 500 이하의 자연수입니다.
'''

command = {'U' : [-1, 0], 'D' : [1, 0], 'R' : [0, 1], 'L' : [0, -1]}
cp = [[''] * 11 for _ in range(11)]

def solution(dirs):
    cnt = 0
    x, y = 5, 5

    for i in dirs:
        if i == 'U':
            cp[x][y] += 'D'

        elif i == 'D':
            cp[x][y] += 'U'

        elif i == 'R':
            cp[x][y] += 'L'

        else:
            cp[x][y] += 'R'

        x += command[i][0]
        y += command[i][1]

        if 0 <= x < 11 and 0 <= y < 11:
            if i not in cp[x][y]:
                cp[x][y] += i
                cnt += 1

        else:
            x -= command[i][0]
            y -= command[i][1]
            cp[x][y] = cp[x][y][:-1]

    return cnt

print(solution("ULURRDLLU"))    # 7
print(solution("LULLLLLLU"))    # 7
print(solution("UDU"))          # 1

'''
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
'''