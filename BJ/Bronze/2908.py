N, M = map(str, input().split())

print(max(N[::-1], M[::-1]))

# 숫자는 인덱싱 안되고 글자는 됨!