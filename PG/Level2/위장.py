from collections import defaultdict

def solution(clothes):
    c_dict = defaultdict(list)
    ans = 1

    for i in clothes:
        c_dict[i[1]].append(i[0])

    for j in c_dict:
        ans *= len(c_dict[j]) + 1

    return ans - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))