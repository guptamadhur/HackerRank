# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

def count_substring(string, sub_string):
    count = 0
    k = len(sub_string)
    for i in range(0, len(string)):
        sub_str = string[i:i + k]
        print(sub_str)
        if sub_str == sub_string:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)