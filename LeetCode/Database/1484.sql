Select sell_date, Count(Distinct product) as num_sold, Group_Concat(Distinct product Order By product) as products
From Activities
Group By sell_date;

-- MySQL에서 group by로 문자열을 합칠 땐 group_concat 이용
-- 1. 기본형 : group_concat(필드명)
-- 2. 구분자 변경 : group_concat(필드명 separator '구분자')
-- 3. 중복제거 : group_concat(distinct 필드명)
-- 4. 문자열 정렬 : group_concat(필드명 order by 필드명)

-- 출처: https://fruitdev.tistory.com/16