import sys
N = int(sys.stdin.readline().rstrip())
books = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if word not in books:
        books[word] = 1

    else:
        books[word] += 1

books = sorted(books.items(), key= lambda item: item[1], reverse=True)
num = books[0][1]

for i in range(len(books)):
    if books[i][1] < num:
        books = books[:i]
        break

books = sorted(books, key= lambda x: x[0])
print(books[0][0])

'''
a = []
for _ in range(int(input())):
    a.append(input())

# 여기서 정렬 끝났고
a.sort()

# 여기서 갯수 최대치 끝났고
print(max(set(a), key=a.count))

# 정렬이 되어있으니까 첫번째 걸리는 (알파벳상 가장 앞) 것이 출력!
'''