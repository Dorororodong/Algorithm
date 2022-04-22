Select U.name, Ifnull(Sum(R.distance), 0) as travelled_distance
From Users as U
Left Join Rides as R
On U.id = R.user_id
Group By U.id
Order By Sum(R.distance) Desc, U.name;

-- 참고 : https://velog.io/@gillog/DB-MySQL-NULL-%EC%B2%98%EB%A6%ACIFNULL-CASE-COALESCE


-- SELECT
--    CASE
--        WHEN NAME IS NULL THEN "No name"
--        ELSE NAME
--    END as NAME
-- FROM ANIMAL_INS


-- SELECT COALESCE(Column명1, Column명1이 NULL인 경우 대체할 값)
-- FROM 테이블명