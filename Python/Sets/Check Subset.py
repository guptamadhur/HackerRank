# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    for _ in range(int(input())):
        numA = int(input())
        A = set(map(int, input().split()))
        numB = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))