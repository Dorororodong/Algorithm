'''
항상 "ICN" 공항에서 출발
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''

# DFS!

def solution(tickets):
    answer = []
    stack = ['ICN']     # 무조건 인천 시작
    dict = {}           # 딕셔너리 느낌으로 하면 출-도 형태 / 시간단축?!

    for ticket in tickets:
        if ticket[0] in dict:
            dict[ticket[0]].append(ticket[1])
        else:
            dict[ticket[0]] = [ticket[1]]       # 리스트로 해야만 추가가 됨

    '''
    {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    '''

    # 도움을 얻은 Point (pop이 뒤에서부터 빼오니까)
    for i in dict:
        dict[i].sort(reverse=True)

    while stack:
        top = stack[-1] # stack으로부터 찾아나서기

        if top in dict and len(dict[top]) != 0: # 해당하고, 도착지 선택지가 있다면!
            stack.append(dict[top].pop())       # 빼서 스택에 담고!

        else:
            answer.append(stack.pop())          # 없으면 정답 경로에 스택을 빼서 담음!

    return  answer[::-1]        # 도움을 얻은 Point (stack에서 역순으로 답에 집어넣으니까)

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# ["ICN", "JFK", "HND", "IAD"]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
