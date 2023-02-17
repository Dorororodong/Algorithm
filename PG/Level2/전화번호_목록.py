def solution(phone_book):
    pb_set = {}

    for i in phone_book:
        pb_set[i] = True

    for i in pb_set:
        prefix = ''

        for j in i:
            prefix += j

            if prefix in pb_set and prefix != i:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))