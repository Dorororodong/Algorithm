'''
SELECT IF(g.Grade < 8, NULL, s.Name), g.Grade, s.Marks
FROM Students as s
INNER JOIN Grades as g
ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC, s.Name, s.Marks;
'''