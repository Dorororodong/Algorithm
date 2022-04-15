'''
# 중성화를 안하면 성별이 그대로고, 하면 달라짐
Select ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
From ANIMAL_INS as ins
Inner Join ANIMAL_OUTS as outs
On ins.ANIMAL_ID = outs.ANIMAL_ID
Where ins.SEX_UPON_INTAKE != outs.SEX_UPON_OUTCOME
Order By ins.ANIMAL_ID;

# 조건을 그대로 반영
# WHERE A.SEX_UPON_INTAKE LIKE 'INTACT%'
# AND (B.SEX_UPON_OUTCOME LIKE 'SPAYED%'
# OR B.SEX_UPON_OUTCOME LIKE 'NEUTERED%')
'''