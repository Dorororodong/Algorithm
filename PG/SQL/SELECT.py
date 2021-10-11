'''
# 모든 레코드 조회하기
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID

# 역순 정렬하기
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC

# 아픈 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick'

# 어린 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID

# 동물의 아이디와 이름
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID

# 여러 기준으로 정렬하기
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC

# 상위 n개 레코드
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1

'''