Select product_id, 'store1' as store, store1 as price
From Products
Where store1 is Not Null
union
Select product_id, 'store2' as store, store2 as price
From Products
Where store2 is Not Null
union
Select product_id, 'store3' as store, store3 as price
From Products
Where store3 is Not Null;

-- union : [distinct], 중복 제거
-- union all : 모든 컬럼 값을 보여줌, 중복 제거 X