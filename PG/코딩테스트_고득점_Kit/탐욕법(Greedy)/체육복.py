'''
전체 학생의 수는 2명 이상 30명 이하
도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''

def solution(n, lost, reserve):
   
    set_reserve = set(reserve) - set(lost)  # 초기세팅
    set_lost = set(lost) - set(reserve)     # 여분있어도 강탈당하면 둘다 제거!

    for i in set_reserve:               # 여분친구들
        if i-1 in set_lost:             # 앞번호
            set_lost.remove(i-1)
        elif i+1 in set_lost:           # 뒷번호
            set_lost.remove(i+1)
    return n-len(set_lost)              # 전체에서 그래도 참가못하는 제거

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3]))   # 4
print(solution(3, [3], [1]))  # 2
print(solution(3, [1, 2, 3], [1, 2, 3]))  # 3