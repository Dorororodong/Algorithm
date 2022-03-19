import sys
word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
N = len(bomb)

for i in word:
    stack.append(i)

    # res 만들 때는 비교용도니까, 그만큼만 제작 해주면 된다! (길면 길어질수록 시간 많이 걸림!)
    # res = "".join(stack[-N:])

    # 마지막 글자 일치여부부터 확인 / and 니까 앞에서 안되면 뒤에 안 봄 / 뒤에는 그 때만 join 실행 (심지어 그 부분만)
    if bomb[-1] == i and bomb == "".join(stack[-N:]):
        # for _ in range(N):
        #     stack.pop()

        del stack[-N:] # (위의 for문 대체 가능) / Python 예약어 : if, for 같이...

if len(stack) > 0:
    print("".join(stack))

else:
    print("FRULA")