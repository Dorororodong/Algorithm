SELECT d.name as Department, e.name as Employee, e.salary
FROM Employee as e
INNER JOIN Department as d
ON e.departmentId = d.id
WHERE 3 > (SELECT COUNT(DISTINCT e2.salary) FROM Employee as e2 WHERE e2.salary > e.salary AND e.departmentId = e2.departmentId);

------------------------------------------------------------------------------------------------------------------------------------------------------

SELECT d.name as Department, e.name as Employee, e.salary
FROM Employee as e
INNER JOIN Department as d
ON e.departmentId = d.id
WHERE e.salary IN (SELECT * FROM (SELECT DISTINCT(salary) FROM Employee WHERE departmentId = d.id ORDER BY salary DESC LIMIT 3) as _);

-- 참고 : https://codingspooning.tistory.com/entry/leetcode-MySQL-185-Department-Top-Three-Salaries