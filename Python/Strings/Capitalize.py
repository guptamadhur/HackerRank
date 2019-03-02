# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input
#
# chris alan
# Sample Output
#
# Chris Alan

def solve(s):
    return(' '.join(i.capitalize() for i in s.split(' ')))

if __name__ == '__main__':
    print(solve(input()))