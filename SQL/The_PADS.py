'''
Select Concat(Name, '(', Substr(Occupation, 1, 1), ')')
From OCCUPATIONS
Order By Name;

Select Concat('There are a total of ', Count(Occupation), ' ', Lower(Occupation), 's.')
From OCCUPATIONS
Group By Occupation
Order By Count(Occupation), Occupation;

# Concat : 문자열들을 합체!
# Substr : (해당컬럼, 시작위치, 갯수[시작위치 포함 / 적지 않으면 끝까지])
# Lower : 모두 소문자로, Upper : 모두 대문자로
# Group By : 유형별로 갯수를 알고 싶을 때, 컬럼에 데이터를 그룹화 할 수 있음
# Having : 특정 컬럼을 그룹화한 결과에 조건을 걸 때 (Where이 아님)
'''

'''
# Left도 가능 1글자니까!
Select Concat(Name, '(', Left(Occupation, 1), ')')
From OCCUPATIONS
Order By Name;

Select Concat('There are a total of ', Count(Occupation), ' ', Lower(Occupation), 's.')
From OCCUPATIONS
Group By Occupation
Order By Count(Occupation), Occupation;
'''