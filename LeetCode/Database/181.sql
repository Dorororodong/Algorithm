SELECT e.name as Employee
FROM Employee as e
LEFT JOIN Employee as m
ON e.managerId = m.id
WHERE e.salary > m.salary;

-- SELECT
--     a.Name AS 'Employee'
-- FROM
--     Employee AS a,
--     Employee AS b
-- WHERE
--     a.ManagerId = b.Id
--         AND a.Salary > b.Salary;

-- SELECT
--      a.NAME AS Employee
-- FROM Employee AS a JOIN Employee AS b
--      ON a.ManagerId = b.Id
--      AND a.Salary > b.Salary;