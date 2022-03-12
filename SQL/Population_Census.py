'''
# 1
Select Sum(I.POPULATION)
From CITY As I, COUNTRY As O
Where I.COUNTRYCODE = O.CODE And O.CONTINENT = 'Asia';

# 2
SELECT SUM(City.population)
FROM City
	INNER JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Continent = 'Asia'

# 3
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE IN (SELECT CODE
                    FROM COUNTRY
                    WHERE CONTINENT='Asia'
                );

# 참고 사이트 : https://pearlluck.tistory.com/46
'''