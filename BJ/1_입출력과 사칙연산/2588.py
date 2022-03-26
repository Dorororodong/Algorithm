a = int(input())
b = int(input())

print(a * (b % 10))
print(a * ((b // 10) % 10))
print(a * (b // 100))
print(a * b)

'''
a = input()
b = input()

print(int(a)*int(b[-1]))
print(int(a)*int(b[-2]))
print(int(a)*int(b[-3]))
print(int(a)*int(b))
'''