'''
SELECT R.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW R
LEFT JOIN REST_INFO I
ON R.REST_ID = I.REST_ID
GROUP BY R.REST_ID
HAVING I.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, I.FAVORITES DESC;


1. JOIN... 기준은?!...
2. AVG - GROUP BY - HAVING : REST_REVIEW 기준!
3. 1가게 - 많은 리뷰 : 가게를 GROUP BY
4. ALIAS(SCORE)를 ORDER BY에는 쓸 수 있음
'''