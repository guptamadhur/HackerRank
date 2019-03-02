# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input
#
# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Sample Output
#
# 5
# 9
# 11
# 12

if __name__ == '__main__':
    a, b = [set(input().split()) for _ in range(4)][1::2]
    print('\n'.join(sorted(a ^ b, key=int)))
