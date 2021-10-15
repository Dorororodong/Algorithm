'''
# 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(*) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE


# 동명 동물 수 찾기
### SELECT NAME, COUNT(*) FROM ANIMAL_INS WHERE NOT NAME is NULL GROUP BY NAME HAVING COUNT(*) > 1 ORDER BY NAME ###

### WHERE NOT 컬럼 is NULL ###

### GROUP BY 컬럼 HAVING 조건 ###


# 입양 시각 구하기(1)
?


# 입양 시각 구하기(2)
?


'''