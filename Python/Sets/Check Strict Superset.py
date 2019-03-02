# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    a = set(input().split())
    print(all(a > set(input().split()) for _ in range(int(input()))))