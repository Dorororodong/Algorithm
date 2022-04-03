'''
SELECT Hour(DATETIME) as HOUR, Count(DATETIME) as COUNT
FROM ANIMAL_OUTS
GROUP BY Hour(DATETIME)
HAVING HOUR >= 9 and HOUR < 20
Order By HOUR;

# YEAR : 연도 추출
# MONTH : 월 추출
# DAY : 일 추출 (DAYOFMONTH와 동일)
# HOUR : 시 추출
# MINUTE : 분 추출
# SECOND : 초 추출
'''