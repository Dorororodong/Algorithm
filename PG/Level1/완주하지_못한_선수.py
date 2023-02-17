from collections import defaultdict

def solution(participant, completion):
    p_set = defaultdict(int)

    for i in participant:
        p_set[i] += 1

    for j in completion:
        p_set[j] -= 1

    for (k, l) in p_set.items():
        if l > 0:
            return k

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))