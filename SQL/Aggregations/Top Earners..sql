# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select (months*salary), count(*) from Employee group by (months*salary) DESC LIMIT 1