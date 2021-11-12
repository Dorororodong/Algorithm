for _ in range(10):
    tc = int(input())
    find_word = input()
    target_word = input()
    print('#{} {}'.format(tc, target_word.count(find_word)))