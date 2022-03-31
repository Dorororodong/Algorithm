'''
Select NAME, Count(NAME)
From ANIMAL_INS
Group By NAME
Having Count(NAME) > 1
Order By NAME;

# Group By의 조건절은 Having!
'''