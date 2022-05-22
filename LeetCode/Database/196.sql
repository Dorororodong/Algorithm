DELETE p1
FROM Person as p1
INNER JOIN person as p2
ON p1.email = p2.email
WHERE p1.id > p2.id;

-- DELETE FROM 테이블 WHERE 조건식