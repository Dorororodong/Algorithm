'''
한 번에 한 개의 알파벳만 바꿀 수 있습니다.
words에 있는 단어로만 변환할 수 있습니다.

각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
'''

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    else:
        
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# 4
# 0