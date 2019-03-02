# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Sample Input
#
# AABCAAADA
# 3
# Sample Output
#
# AB
# CA
# AD

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)  # get length of a string
    strings_list = []
    for i in range(0, n, k):
        sub_string = string[i:i + k]
        short_string = ""
        for j in sub_string:
            if j not in short_string:
                short_string += j
        strings_list.append(short_string)
    print(*strings_list, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)