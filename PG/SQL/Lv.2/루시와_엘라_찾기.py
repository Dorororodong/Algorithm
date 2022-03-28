'''
# ~ In (, , , , ...)

Select ANIMAL_ID, NAME, SEX_UPON_INTAKE
From ANIMAL_INS
Where NAME In ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
Order By ANIMAL_ID;


# ~ = ! Or ~ = ! Or ~ = ! Or ...

Select ANIMAL_ID, NAME, SEX_UPON_INTAKE
From ANIMAL_INS
Where NAME = 'Lucy' Or NAME = 'Ella' Or NAME = 'Pickle' Or NAME = 'Rogan' Or NAME = 'Sabrina' Or NAME = 'Mitty'
Order By ANIMAL_ID;
'''