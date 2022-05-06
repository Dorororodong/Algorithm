SELECT id, if(p_id is null, 'Root', if(id in (SELECT p_id FROM Tree), 'Inner', 'Leaf')) as type
FROM Tree
ORDER BY id;