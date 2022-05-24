SELECT d.name as Department, e.name as Employee, e.salary
FROM Employee as e
INNER JOIN Department as d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) in (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId);

-- 참고 : https://pearlluck.tistory.com/492