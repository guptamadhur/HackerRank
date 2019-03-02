# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))