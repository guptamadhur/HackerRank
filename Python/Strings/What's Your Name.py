# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input 0
#
# Ross
# Taylor
# Sample Output 0
#
# Hello Ross Taylor! You just delved into python.
# Explanation 0
#
# The input read by the program is stored as a string data type. A string is a collection of characters.

def print_full_name(a, b):
    print (("Hello %s %s! You just delved into python.") % (first_name, last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)