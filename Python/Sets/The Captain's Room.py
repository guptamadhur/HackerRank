# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    k,arr = int(input()),list(map(int, input().split()))
    myset = set(arr)
    print(((sum(myset)*k)-(sum(arr)))//(k-1))