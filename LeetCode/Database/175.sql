SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address as a
ON p.personId = a.personId;

-- Considering there might not be an address information for every person, we should use outer join instead of the default inner join.
-- 모든 사람에 대한 주소 정보가 없을 수 있으므로 기본 내부 조인 대신 외부 조인을 사용해야 함 (Null이 조회가 안되고/되고)