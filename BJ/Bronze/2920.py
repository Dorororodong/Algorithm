scale = list(map(int, input().split()))

if scale == sorted(scale):
    print('ascending')

elif scale[::-1] == sorted(scale):
    print('descending')

else:
    print('mixed')