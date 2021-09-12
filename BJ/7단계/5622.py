word = input()
total = 0

for i in word:
    if i in ['A', 'B', 'C']:
        total += 3
    elif i in ['D', 'E', 'F']:
        total += 4
    elif i in ['G', 'H', 'I']:
        total += 5
    elif i in ['J', 'K', 'L']:
        total += 6
    elif i in ['M', 'N', 'O']:
        total += 7
    elif i in ['P', 'Q', 'R', 'S']:
        total += 8
    elif i in ['T', 'U', 'V']:
        total += 9
    else:
        total += 10
    
print(total)