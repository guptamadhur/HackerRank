# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Print the modified string .
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    return (''.join([i.lower() if i.isupper() else i.upper() for i in s]))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)