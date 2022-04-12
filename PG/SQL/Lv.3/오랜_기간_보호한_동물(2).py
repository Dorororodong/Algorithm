'''
Select ins.ANIMAL_ID, ins.NAME
From ANIMAL_INS as ins
Inner Join ANIMAL_OUTS as outs
On ins.ANIMAL_ID = outs.ANIMAL_ID
Order By outs.DATETIME - ins.DATETIME Desc
Limit 2;
'''