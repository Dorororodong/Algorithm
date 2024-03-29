'''
# 아닌듯
SELECT F.FLAVOR
FROM FIRST_HALF F
LEFT JOIN JULY J
ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;
'''

'''
SELECT T.FLAVOR
FROM (SELECT * FROM FIRST_HALF 
    UNION ALL
    SELECT * FROM JULY) AS T
GROUP BY T.FLAVOR
ORDER BY SUM(T.TOTAL_ORDER)DESC
LIMIT 3;
'''

'''
SELECT F.FLAVOR
FROM FIRST_HALF F LEFT JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) J ON F.FLAVOR = J.FLAVOR
ORDER BY (F.TOTAL_ORDER + J.TOTAL_ORDER) DESC LIMIT 3;
'''