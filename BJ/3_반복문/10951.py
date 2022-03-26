# try / except 구문... 중요!
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break