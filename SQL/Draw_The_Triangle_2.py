'''
Set @Numbers = 0;
Select Repeat('* ', @Numbers := @Numbers + 1)
From Information_Schema.Tables Limit 20;
'''