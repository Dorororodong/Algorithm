def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree[ord(node) - 65][1])
        pre_order(tree[ord(node) - 65][2])


def in_order(node):
    if node != '.':
        in_order(tree[ord(node) - 65][1])
        print(node, end='')
        in_order(tree[ord(node) - 65][2])


def post_order(node):
    if node != '.':
        post_order(tree[ord(node) - 65][1])
        post_order(tree[ord(node) - 65][2])
        print(node, end='')


import sys
N = int(sys.stdin.readline().rstrip())
tree = [[0] * 3 for _ in range(N)]

for _ in range(N):
    P, L, R = sys.stdin.readline().rstrip().split()
    tree[ord(P) - 65][1] = L
    tree[ord(P) - 65][2] = R

pre_order('A')
print()
in_order('A')
print()
post_order('A')