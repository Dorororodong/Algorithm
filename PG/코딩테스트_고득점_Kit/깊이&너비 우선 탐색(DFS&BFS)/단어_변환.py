'''
한 번에 한 개의 알파벳만 바꿀 수 있습니다.
words에 있는 단어로만 변환할 수 있습니다.

각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
'''

# DFS!

def solution(begin, target, words):
    answer = 0
    stack = []

    if target not in words:     # target이 words에 없으면 변환해서 절대 안나오니까
        return 0

    stack.append(begin)         # 시작을 담고

    while stack:
        for i in (0, len(words)):
            cnt = 0             # 글자 다른 갯수
            for j in range(0, len(begin)):
                if stack[-1][j] != words[i][j]: # 글자가 다르면
                    cnt += 1

                if cnt > 1:     # 1개 넘게 다르면 볼 필요 X
                    break

            if cnt == 1:        # 1개만 다르면
                stack.append(words[i])  # stack에 추가
                answer += 1             # 횟수 1증가

            if stack[-1] == target: # target 도달 시 출력
                return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
# 4
# 0