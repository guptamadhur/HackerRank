# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

n = int(input())

results = []

for i in range(1, n+1):
    decimal = str(i)
    octal = str(oct(i)[2:])
    hex_ = str(hex(i)[2:]).upper()
    binary = str(bin(i)[2:])

    results.append([decimal, octal, hex_, binary])

width = len(results[-1][3])  # largest binary number

for i in results:
    print(*(rep.rjust(width) for rep in i))


# Second Option
    def print_formatted(number):
        w = len(format(number, 'b'))
        for i in range(1, number + 1):
            d = str(i).rjust(w)
        o = format(i, 'o').rjust(w)
        h = format(i, 'x').rjust(w).upper()
        b = format(i, 'b').rjust(w)
        print(d, o, h, b)