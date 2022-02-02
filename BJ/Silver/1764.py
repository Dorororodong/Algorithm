import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

never_heard = set(sys.stdin.readline().rstrip() for _ in range(N))
never_seen = set(sys.stdin.readline().rstrip() for _ in range(M))

never_heard_and_never_seen = sorted(list(never_heard & never_seen))

# print(len(never_heard_and_never_seen))
# for i in never_heard_and_never_seen:
#     print(i)

# 한줄로 정리 가능
print(len(never_heard_and_never_seen), *never_heard_and_never_seen, sep='\n')