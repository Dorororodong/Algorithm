'''
Select *
From PLACES
Where HOST_ID in (Select HOST_ID From PLACES Group By HOST_ID Having Count(HOST_ID) >= 2)
Order By ID;

# HOST_ID들을 보고싶은데, 그 기준이 되는 곳을 다시 in 안에 보여줄 수 있게![해당하는 조건]
'''