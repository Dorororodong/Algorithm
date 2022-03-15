'''
Set @Number = 21;
Select Repeat('* ', @Number := @Number - 1)
From Information_Schema.Tables Limit 20;

# SET : is used with UPDATE to specify which columns and values that should be updated in a table
# REPEAT : 루프의 종료 부분에서 평가되는 조건이 참이 될 때까지 평가되는 명령문의 세트를 정의
# FROM INFORMATION.SCHEMA.TABLES : 테이블 조회
'''