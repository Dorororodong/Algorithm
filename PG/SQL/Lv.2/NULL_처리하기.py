'''
Select ANIMAL_TYPE, IfNULL(NAME, 'No name'), SEX_UPON_INTAKE
From ANIMAL_INS
Order By ANIMAL_ID;

# IfNULL(A, B) : A가 NULL이면 B를, 그렇지 않다면 A를 반환
'''