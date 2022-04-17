Select event_day as day, emp_id, Sum(out_time) - Sum(in_time) as total_time
From Employees
Group By emp_id, event_day;