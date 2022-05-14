SELECT user_id, concat(upper(left(name, 1)), lower(right(name, length(name) - 1))) as name
FROM Users
ORDER BY user_id;

-- https://m.blog.naver.com/dktmrorl/222078571979
-- https://sesok808.tistory.com/491