# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select DISTINCT CITY from STATION WHERE CITY NOT RLIKE "[aeiou]$" AND CITY NOT RLIKE "^[aeiou]";