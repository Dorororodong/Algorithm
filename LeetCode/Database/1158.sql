SELECT user_id as buyer_id, join_date, IFNULL(num, 0) as orders_in_2019
FROM Users
LEFT JOIN (SELECT buyer_id, COUNT(*) as num
          FROM Orders
          WHERE order_date BETWEEN '2019-01-01' and '2019-12-31'
          GROUP BY buyer_id
          ) as t
ON Users.user_id = t.buyer_id;

-- 참고 : https://leetcode.ca/2019-01-31-1158-Market-Analysis-I/
-- BETWEEN A AND B : A이상 B이하
-- IFNULL(컬럼명, NULL일 경우 값)