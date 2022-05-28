SELECT MAX(salary) as SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- https://techblog-history-younghunjo1.tistory.com/155
-- https://wakestand.tistory.com/293
-- https://github.com/Seanforfun/Algorithm-and-Leetcode/blob/master/leetcode/176.%20Second%20Highest%20Salary.md