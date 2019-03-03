# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) from CITY
INNER JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.Continent