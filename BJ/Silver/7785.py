import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
company = defaultdict(int)

for _ in range(n):
    name, access = sys.stdin.readline().rstrip().split()

    if access == 'enter':
        company[name] += 1

    else:
        company[name] -= 1

res = []
yes_no = list(company.values())
who = list(company.keys())

for i in range(len(company)):
    if yes_no[i] > 0:
        res.append(who[i])

res.sort(reverse=True)

for j in res:
    print(j)

# import sys
# n = int(sys.stdin.readline().rstrip())
# res = set()
#
# for _ in range(n):
#     name, access = sys.stdin.readline().rstrip().split()
#
#     if access == 'enter':
#         res.add(name)
#
#     else:
#         res.remove(name)
#
# # print(sorted(res, reverse=True))
# print('\n'.join(sorted(res, reverse=True)))