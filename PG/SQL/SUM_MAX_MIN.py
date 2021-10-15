'''
# 최댓값 구하기
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1


# 최솟값 구하기
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1


# 동물 수 구하기
SELECT COUNT(*) FROM ANIMAL_INS


# 중복 제거하기
### SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NOT NAME is NULL ###

### SELECT (DISTINCT 컬럼) FROM 테이블이름

### WHERE NOT 컬럼 is NULL ###


'''