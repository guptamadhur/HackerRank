# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

SELECT CASE WHEN A+B > C THEN CASE WHEN A=B AND B=C THEN 'Equilateral' WHEN A=B OR B=C OR A=C THEN
'Isosceles' WHEN A !=B OR B !=C or A!=C THEN 'Scalene' END ELSE 'Not A Triangle' END FROM TRIANGLES;