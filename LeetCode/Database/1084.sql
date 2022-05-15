SELECT product_id, product_name
FROM Product
WHERE product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date > '2019-03-31' OR sale_date < '2019-01-01');

-- https://github.com/Ginny47/SQL/blob/main/E-1084.%20Sales%20Analysis%20III