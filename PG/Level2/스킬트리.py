def solution(skill, skill_trees):
    cnt = 0
    for h in skill_trees:
        for i in range(len(skill)-1):
            for j in range(i+1, len(skill)):
                if h.find(skill[i]) == -1 or h.find(skill[j]) == -1:
                    continue
                if h.find(skill[i]) > h.find(skill[j]):
                    break
    cnt += 1
    return cnt

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2