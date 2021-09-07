H, M = map(int, input().split())

if H != 0:
    if M >= 45:
        print(H, M-45)
    else:
        print(H-1, M+15)
else:
    if M >= 45:
        print(H, M-45)
    else:
        print(23, M+15)