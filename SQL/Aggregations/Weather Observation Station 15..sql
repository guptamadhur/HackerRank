# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select round(sum(LONG_W),4) from STATION WHERE LAT_N=(select max(LAT_N) from STATION WHERE LAT_N < 137.2345)