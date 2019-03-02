# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

# Print the runner-up score.
#
# Sample Input 0
#
# 5
# 2 3 6 6 5
# Sample Output 0
#
# 5

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    listnew = []
    for i in arr:
        if i not in listnew:
            listnew.append(i)
    listnew.sort(reverse=True)
    print(listnew[1])

    #Second Way
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))
    print(max(lis))