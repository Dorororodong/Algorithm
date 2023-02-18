'''
SELECT P.MEMBER_NAME , R.REVIEW_TEXT , DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE P
LEFT JOIN REST_REVIEW R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE 1=1
    AND R.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING COUNT(MEMBER_ID) = (SELECT MAX(cnt)
                                            FROM (SELECT COUNT(MEMBER_ID) AS cnt
                                            FROM REST_REVIEW
                                            GROUP BY MEMBER_ID) a))
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT;
'''