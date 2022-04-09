'''
Select ins.ANIMAL_ID, ins.NAME
From ANIMAL_INS as ins
Inner Join ANIMAL_OUTS as outs
On ins.ANIMAL_ID = outs.ANIMAL_ID
Where ins.DATETIME > outs.DATETIME
Order By ins.DATETIME;
'''