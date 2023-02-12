'''
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE 1=1
    AND GENDER = 'W'
    AND MONTH(DATE_OF_BIRTH) = 3
    AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;
'''


'''
SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
TO_CHAR(DATE_OF_BIRTH, 'yyyy-mm-dd') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE TO_CHAR(DATE_OF_BIRTH, 'mm') = '03' 
AND GENDER = 'W'
AND TLNO IS NOT NULL 
ORDER BY MEMBER_ID;
'''