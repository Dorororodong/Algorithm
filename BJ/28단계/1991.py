# 전위 순회 (V -> L -> R)
def pre_order(node, n):
    if node != '.':
        print(node, end='')
        pre_order(tree[n+1][0], n+1)
        pre_order(tree[n+2][1], n+2)

    return

# 중위 순회 (L -> V -> R)
def in_order(node, n):
    if node != '.':
        pre_order(tree[n+1][0], n+1)
        print(node, end='')
        pre_order(tree[n+2][1], n+2)

    return

# 후위 순회 (L -> R -> V)
def post_order(node, n):
    if node != '.':
        pre_order(tree[n+1][0], n+1)
        pre_order(tree[n+2][1], n+2)
        print(node, end='')

    return

import sys
sys.stdin = open('input.txt')

V = int(input())

tree = [[0] * 3 for _ in range(V)]

for tc in range(V):
    P, L, R = input().split()
    tree[tc][0] = L
    tree[tc][1] = R

print(pre_order('A', 0))
print(in_order('A', 0))
print(post_order('A', 0))