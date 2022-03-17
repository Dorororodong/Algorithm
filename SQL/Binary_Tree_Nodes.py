'''
Select N, If(P is null, 'Root', If(BST.N in (Select P From BST), 'Inner', 'Leaf'))
From BST
Order By N;

# [is](=?) null : sql에서 판별식
# From 1번 먹었으면, 그다음은 Table.Colmun
# Select 별 조건 X = 전부
'''