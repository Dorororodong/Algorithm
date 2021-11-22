import sys
dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline().rstrip()))

dwarf.sort()
total = sum(dwarf)

for i in range(8):
    for j in range(i+1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            num1 = dwarf[i]
            num2 = dwarf[j]
            break

dwarf.remove(num1)
dwarf.remove(num2)

for k in dwarf:
    print(k)