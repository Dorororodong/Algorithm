x, y, w, h = map(int, input().split())

min_x = min(x, w-x)
min_y = min(y, h-y)

print(min(min_x, min_y))