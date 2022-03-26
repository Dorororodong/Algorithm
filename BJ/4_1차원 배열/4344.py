T = int(input())

for tc in range(1, T+1):
    cnt = 0
    num_score = list(map(int, input().split()))
    avg = sum(num_score[1:]) / num_score[0]

    for i in num_score[1:]:
        if i > avg:
            cnt+=1
    print('{0:.3f}%'.format(cnt/num_score[0] * 100))


# print(f'{(above/len(scores))*100:.3f}%')
# print('%.3f'%round(sum(map(lambda x:x>mean, a[1:len(a)]))/a[0]*100,4)+"%")
