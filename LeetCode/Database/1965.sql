Select employee_id
From
    (Select employee_id From Employees
     Union all
     Select employee_id From Salaries) as missing
Group By employee_id
Having Count(*) = 1
Order By employee_id;

-- Union all : 전부다 합체 (중복이고 나발이고 전부 다)
-- 둘 중 하나 빠진 친구가 누락 된 것이므로 Count(*) = 1
-- From TABLE 이름 새로 명시!
