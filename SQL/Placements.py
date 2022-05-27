'''
SELECT s.Name
FROM Students as s
INNER JOIN Packages as p1 ON s.ID = p1.ID
INNER JOIN Friends as f ON s.ID = f.ID
INNER JOIN Packages as p2 ON f.Friend_ID = p2.ID
WHERE p1.Salary < p2.Salary
ORDER BY p2.Salary;
'''