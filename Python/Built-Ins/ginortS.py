# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input
# #
# # Sorting1234
# # Sample Output
# #
# # ginortS1324

if __name__== '__main__':
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    print(*sorted(input(), key=order.index), sep='')

    # 3 Other Solution
    print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

    print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

    import string
    print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')