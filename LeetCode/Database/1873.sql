Select employee_id, If(employee_id % 2 = 0 Or Left(name, 1) = 'M', 0, salary) as bonus
From Employees;