Select player_id, Min(event_date) as first_login
From Activity
Group By player_id;