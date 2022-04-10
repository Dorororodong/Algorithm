'''
Select ins.NAME, ins.DATETIME
From ANIMAL_INS as ins
Left Join ANIMAL_OUTS as outs
On ins.ANIMAL_ID = outs.ANIMAL_ID
Where outs.ANIMAL_ID is Null
Order By ins.DATETIME
Limit 3;

# ins에는 있지만, outs에는 없는
# 참고 : https://pearlluck.tistory.com/46
'''