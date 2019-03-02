# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    n, m = input().split()
    arrayElement = input().split()
    A = set(input().split())
    B = set(input().split())

    print(sum([(i in A) - (i in B) for i in arrayElement]))