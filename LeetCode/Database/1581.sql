-- On 부분은 교집합! / 아닌 거 찾을 때는 조건문에!
Select V.customer_id, Count(*) as count_no_trans
From Visits as V
Left Join Transactions as T
On V.visit_id = T.visit_id
Where T.visit_id is Null
Group By V.customer_id;

-- Select customer_id, Count(*) as count_no_trans
-- From Visits
-- Where visit_id Not in (Select visit_id From Transactions Group By visit_id)
-- Group By customer_id;