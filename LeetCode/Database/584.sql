SELECT name
FROM Customer
WHERE referee_id != 2 or referee_id is null;

-- = null (X)
-- is null (O)
-- != = <>