'''
Select Distinct CITY
From STATION
Where CITY REGEXP '^[^aeiou]';
^ : []밖에 있을 때는 시작하는 문자열이지만, 그 []안에서 ^하는 것은 부정을 뜻함
'''