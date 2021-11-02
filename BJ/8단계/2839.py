N = int(input())

cnt = -1        # 안될 때도 생각

if N >= 5:                              # N = 18?
    for i in range(N//5, -1, -1):       # 3~0
        if (N - 5 * i) % 3 == 0:        # 5가 3봉지고, 나머지가 3의배수이여야함
            cnt += i                    # +3, 5봉지 갯수 추가
            cnt += (N - 5 * i) // 3     # +1, 나머지에서 3봉지의 갯수 추가
            cnt += 1                    # 보정
            break
    print(cnt)            
else:
    if N == 3:
        print(1)
    else:
        print(-1)


# n = int(input())
# cnt = 0

# while True:
#         if n == 0:
#             print(cnt)
#             break
#         elif n < 0:
#             print(-1)
#             break
#         if (n-5) % 3 == 0 or (n-5) % 5 == 0:
#             n -= 5
#             cnt += 1
#         else:
#             n -= 3
#             cnt += 1