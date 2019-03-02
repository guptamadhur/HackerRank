# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    n = int(input())
    A = set(map(int,input().split()))

    n = int(input())
    B = set(map(int, input().split()))

    print(len(A.difference(B)))