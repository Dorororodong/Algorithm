UPDATE Salary
SET sex = if(sex = 'f', 'm', 'f');

-- UPDATE Salary
-- SET sex = (CASE
--             WHEN sex = 'm'
--             THEN 'f'
--             ELSE 'm'
--             END);

-- UPDATE 테이블명 SET 컬럼명 = 데이터값 WHERE 조건