# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input 0
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


def wrap(st, n):
    s=''
    for i in range(0, len(st) , n):
        s= s.strip() + '\n'+st[i:i + n]
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#With Test Wrap
    import textwrap
    l = " ".join(textwrap.wrap(string, max_width))
    print(textwrap.fill(l, max_width))
