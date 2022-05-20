-- 블로그 참고 : https://codingspooning.tistory.com/entry/leetcode-MySQL-178-Rank-Scores
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores;


-- 릿코드 참고
SELECT s1.score, COUNT(s2.score) as rank FROM Scores as s1,
(SELECT DISTINCT score FROM Scores) as s2
WHERE s1.score <= s2.score
GROUP BY s1.id
ORDER BY s1.score DESC;