# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input
#
# this is a string
# Sample Output
#
# this-is-a-string


def split_and_join(line):
    # write your code here
    return line.replace(" ","-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)