import sys

word = sys.stdin.readline().rstrip()

cnt = 0

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    if i in word:
        cnt += word.count(i)
        word = word.replace(i, " " * len(i))
        # .replace! 주의!

word = word.replace(' ', '')
print(cnt + len(word))

'''
n = input()
c = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in c:
    n = n.replace(i,'A')
print(len(n))
# 그냥 해당하는 문자를... 1개로 바꿨다면... 너무 어렵게 생각...
'''