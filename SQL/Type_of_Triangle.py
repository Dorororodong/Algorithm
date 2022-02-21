'''
Select Case
    When A = B And B = C Then 'Equilateral'
    When A + B <= C or B + C <= A or C + A <= B Then 'Not A Triangle'
    When A = B Or B = C Or C = A Then 'Isosceles'
    Else 'Scalene' End
From TRIANGLES;

# 조건문은 제일 위에서 내려오고, 위에서 걸러진 조건은 밑에서는 영향력이 없음
# Case ~ End
# When 조건 Then 결과 / 그 외의 것은 Else 결과
# 삼각형 조건은... 알아서 하시고요...
'''