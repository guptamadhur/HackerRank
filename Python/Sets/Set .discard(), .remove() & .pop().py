# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

if __name__ == '__main__':
    n = int(input())
    s = set(map(int,input().split()))

    for i in range(int(input())):
        command= input()
        if(command == 'pop'):
            s.pop()
        else:
            command,nums = command.split()
            if (command == 'discard'):
                s.discard(int(nums[0]))
            elif (command == 'remove'):
                b = int(nums[0])
                s.remove(b)
    print(sum(s))