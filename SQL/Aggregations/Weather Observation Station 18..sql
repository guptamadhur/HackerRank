# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select round(round(max(LAT_N)-min(LAT_N),4) + round(max(LONG_W)-min(LONG_W),4),4) from STATION