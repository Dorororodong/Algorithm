SELECT a.id
FROM Weather as a
INNER JOIN Weather as b
ON DATEDIFF(a.recordDate, b.recordDate) = 1 AND a.temperature > b.temperature;

-- DATEDIFF() 함수는 두개의 날짜값의 차이를 int로 반환하는 Mssql 내장함수
-- SELECT DATEDIFF('구분자','Start_Date','End_Date')
-- '구분자'는 어떤차이를 구할지 정해주는 부분이다. / Ex. 두 날짜사이의 날짜 차이를 구하고 싶으면 'day' 혹은 'dd'등을 넣어주면 된다.
-- 한 테이블 내에서 비교 추출 시에는 같은 테이블끼리 JOIN해서 풀면?!
-- https://codingspooning.tistory.com/126