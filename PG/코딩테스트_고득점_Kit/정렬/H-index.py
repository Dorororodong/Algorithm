'''
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
'''
def solution(citations):
    answer = 0

    for i in range(len(citations), 0, -1):  # 최대값을 구하기 위해 길이부터 시작 
        cnt = 0                             # 갯수를 비교하기 위해
        for j in citations:
            if j >= i:                      # 예를 들어 3이상인거 구할 때 3,4,5는
                cnt += 1                    # 갯수 +=1
        if cnt >= i:                        # 중요! : H-index의 의미, 3이상인 총갯수가 3이아니라! 3이상인가?!
            answer += i
            break
    
    return answer

'''
# 영특
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 천재
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''

print(solution([3, 0, 6, 1, 5]))    # 3
print(solution([1, 1, 3]))
print(solution([1, 1, 1, 1, 1, 1]))
print(solution([0, 0, 0, 0, 0, 1]))
print(solution([0, 0, 0, 0, 0, 0]))
print(solution([4, 4, 4, 4, 5]))