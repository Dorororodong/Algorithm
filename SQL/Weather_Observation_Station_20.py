'''
# Oracle
Select Round(Median(LAT_N), 4)
From STATION;

# MySQL
Select Round(LAT_N, 4)
From STATION As S
Where (Select Count(*) From STATION Where LAT_N < S.LAT_N) = (Select Count(*) From STATION Where LAT_N > S.LAT_N);

# Oracle vs MySQL...
# 멀 쓸지 모르니까 둘다 알아야!
'''