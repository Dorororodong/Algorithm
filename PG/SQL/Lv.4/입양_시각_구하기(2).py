'''
Set @HOUR = -1;
Select (@HOUR := @HOUR + 1) as HOUR, (Select Count(Hour(DATETIME)) From ANIMAL_OUTS Where Hour(DATETIME) = @HOUR) as COUNT
From ANIMAL_OUTS
Where @HOUR < 23;

# Set @변수명 = 값; [SET은 어떤 변수에 특정 값을 할당할때 쓰는 명령어 (@ 필수)]
# @변수명 := @변수명 ~ (:=)
'''