from collections import defaultdict

def solution(genres, plays):
    dict1 = defaultdict(int)
    dict2 = defaultdict(list)
    ans = []
    n = len(genres)

    for i in range(n):
        dict1[genres[i]] += plays[i]
        dict2[genres[i]].append((plays[i], i))

    for i in sorted(dict1.items(), key=lambda x : x[1], reverse=True):
        for j in sorted((dict2[i[0]]), key=lambda x: x[0], reverse=True)[:2]:
            ans.append(j[1])

    return ans

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))