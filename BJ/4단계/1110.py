N = int(input())
cnt = 0
S = N

while S != N or cnt == 0:
    cnt += 1 
    if N < 10:
        N = 10 * N + N
        
    else:
        N = 10 * (N%10) + (((N%10) + (N//10))%10)
        
print(cnt)

# n = int(input())
# m = n
# i = 0
# while True:
#     m = m % 10 * 10 + (m % 10 + m // 10) % 10
#     i += 1
#     if m == n:
#         break
# print(i)