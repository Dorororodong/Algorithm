'''
순위	        당첨 내용
1	        6개 번호가 모두 일치
2	        5개 번호가 일치
3	        4개 번호가 일치
4	        3개 번호가 일치
5	        2개 번호가 일치
6(낙첨)	    그 외
'''

def solution(lottos, win_nums):
    answer = []
    zero_cnt = lottos.count(0)
    cnt = 0
    lottos.sort()

    for i in lottos[zero_cnt:]:
        if i in win_nums:
            cnt += 1

    if cnt + zero_cnt <= 1:
        answer.append(6)

        if cnt <= 1:
            answer.append(6)
        else:
            answer.append(7-cnt)

    else:
        answer.append(7 - cnt - zero_cnt)

        if cnt <= 1:
            answer.append(6)
        else:
            answer.append(7-cnt)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))      # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))       # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))       # [1, 1]

'''
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''

'''

2
3
4
5
6
7
8
9
10
11
12
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
'''