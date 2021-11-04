'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

s는 길이 1 이상인 문자열입니다.
s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다.
'''

def solution(s):
    result_list = []
    word = ''
    for i in s:
        if i != ' ':
            word += i
        else:
            result_list.append(word.capitalize())
            word = ''
    result_list.append(word.capitalize())

    return ' '.join(result_list)

print("3people unFollowed me")      # "3people Unfollowed Me"
print("for the last week")          # "For The Last Week"