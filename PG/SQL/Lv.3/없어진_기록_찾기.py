'''
Select outs.ANIMAL_ID, outs.NAME
From ANIMAL_OUTS as outs
Left Join ANIMAL_INS as ins
On outs.ANIMAL_ID = ins.ANIMAL_ID
Where ins.ANIMAL_ID is Null
Order By outs.ANIMAL_ID;

# 참고 : https://pearlluck.tistory.com/46
'''