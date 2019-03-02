# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    for i in range(int(input())):
        try:
            a,b = map(int,input().split())
            print(a//b)
        except BaseException as e:
            print("Error Code:",e)