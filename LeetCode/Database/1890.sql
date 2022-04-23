Select user_id, Max(time_stamp) as last_stamp
From Logins
Where Year(time_stamp) = 2020
Group By user_id;