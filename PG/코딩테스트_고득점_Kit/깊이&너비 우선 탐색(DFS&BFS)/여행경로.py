'''
항상 "ICN" 공항에서 출발
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''

def solution(tickets):
    answer = []
    stack = []

    for i in tickets:
        if i[0] == 'ICN':
            stack.append(i)
            answer.append(i[0])
            tickets.remove(i)
            break
            
    for i in tickets:
        if i[0] == stack[-1][1]:
            answer.append(i[1])
            solution(tickets)
    
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# ["ICN", "JFK", "HND", "IAD"]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]