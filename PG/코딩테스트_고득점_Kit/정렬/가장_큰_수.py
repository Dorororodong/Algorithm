'''
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)   # 사진 참조
    # 221과 2의 비교 : 221 2 / 221221 22 / 221221221 222(여기서 2가!)
    
    return str(int(''.join(numbers)))   # 000이런거 0만들기 위해 int!

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

# "6210"
# "9534330"