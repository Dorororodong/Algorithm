Select id,
    Sum(Case When month = 'Jan' Then revenue End) as Jan_Revenue,
    Sum(Case When month = 'Feb' Then revenue End) as Feb_Revenue,
    Sum(Case When month = 'Mar' Then revenue End) as Mar_Revenue,
    Sum(Case When month = 'Apr' Then revenue End) as Apr_Revenue,
    Sum(Case When month = 'May' Then revenue End) as May_Revenue,
    Sum(Case When month = 'Jun' Then revenue End) as Jun_Revenue,
    Sum(Case When month = 'Jul' Then revenue End) as Jul_Revenue,
    Sum(Case When month = 'Aug' Then revenue End) as Aug_Revenue,
    Sum(Case When month = 'Sep' Then revenue End) as Sep_Revenue,
    Sum(Case When month = 'Oct' Then revenue End) as Oct_Revenue,
    Sum(Case When month = 'Nov' Then revenue End) as Nov_Revenue,
    Sum(Case When month = 'Dec' Then revenue End) as Dec_Revenue
From Department
Group By id;

-- Case(시작) 컬럼 When 비교값이면 Then 출력값 Else 아니면 출력값 End(종료)
-- Case(시작) When 조건 Then 맞으면 값 Else 아니면 값 End(종료)