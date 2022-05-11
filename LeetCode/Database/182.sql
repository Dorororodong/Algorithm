-- 895 ms
SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;

-- 290 ms
SELECT email as Email
FROM (SELECT email, COUNT(email) as num FROM Person GROUP BY email) as statistic
WHERE num > 1;