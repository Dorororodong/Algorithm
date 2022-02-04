import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
site_pwd = {}

for _ in range(N):
    site, pwd = sys.stdin.readline().rstrip().split()
    site_pwd[site] = pwd
    # print(site_pwd)

for _ in range(M):
    find_site = sys.stdin.readline().rstrip()
    print(site_pwd[find_site])