# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

import calendar
if __name__ == '__main__':
    m,d,y=map(int,input().split())
    print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
