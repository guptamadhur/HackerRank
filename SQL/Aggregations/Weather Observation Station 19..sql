# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select round(sqrt(
  round(power((max(LAT_N)-min(LAT_N)),2),4) +
  round(power((max(LONG_W)-min(LONG_W)),2),4)),4) from STATION