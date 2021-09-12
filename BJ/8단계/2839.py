N = int(input())

cnt = -1

if N >= 5:
    for i in range(N//5, -1, -1):
        if (N - 5 * i) % 3 == 0:
            cnt += i
            cnt += (N - 5 * i) // 3
            cnt += 1
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