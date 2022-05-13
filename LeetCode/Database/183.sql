SELECT c.name as Customers
FROM Customers as c
WHERE c.id NOT IN (SELECT o.customerId FROM Orders as o);

-- SELECT c.name as Customers
-- FROM Customers as c
-- LEFT JOIN Orders as o
-- ON c.id = o.customerId
-- WHERE o.customerId IS NULL;