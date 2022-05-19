SELECT CASE
    WHEN id % 2 = 0 THEN id - 1
    WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM seat) THEN id + 1
    ELSE id
    END as id, student
FROM Seat
ORDER BY id;

-- 참고 : https://joke00.tistory.com/103