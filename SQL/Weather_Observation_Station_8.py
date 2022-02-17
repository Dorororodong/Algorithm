'''
Select Distinct CITY
From STATION
Where (CITY Like 'A%' Or CITY Like 'E%' Or CITY Like 'I%' Or CITY Like 'O%' Or CITY Like 'U%') And (CITY Like '%a' Or CITY Like '%e' Or CITY Like '%i' Or CITY Like '%o' Or CITY Like '%u');
'''

'''
# MySQL에서 정규식!!
Select Distinct CITY
From STATION
Where CITY REGEXP '^[aeiou].*[aeiou]$'; 
^ : 시작하는 문자열을 찾음
$ : 끝나는 문자열을 찾음
[] : 안에 나열된 패턴에 해당하는 문자열을 찾음
. : 문자 (점 갯수만큼)
* : 0회 이상 나타나는 문자
'''