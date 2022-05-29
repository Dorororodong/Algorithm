SELECT DISTINCT t1.*
FROM Stadium as t1, Stadium as t2, Stadium as t3
WHERE (t1.people >= 100 AND t2.people >= 100 AND t3.people >= 100)
    AND ((t1.id - t2.id = 1 AND t1.id - t3.id = 2 AND t2.id - t3.id = 1)
        OR (t2.id - t1.id = 1 AND t2.id - t3.id = 2 AND t1.id - t3.id = 1)
        OR (t3.id - t2.id = 1 AND t3.id - t1.id = 2 AND t2.id - t1.id = 1))
ORDER BY t1.id;