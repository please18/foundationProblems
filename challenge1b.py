# Again create pascal's triangle to as many rows as a user requests
# This time print the numbers to the commandline (without turtles)
# E.G.:
#1
#11
#121
#1331
# Coded by Saffa. It is now working. 
import math


def exa(z):
    n = z
    r = 0
    example = ""
    while r <= n:
        fact_n = math.factorial(n)
        fact_r = math.factorial(r)
        sub = n - r
        fact_sub = math.factorial(sub)
        answer = (fact_n / (fact_sub * fact_r))
        example += str(answer) + "  "

        r += 1

    print example


def main():
    n = int(raw_input(" Enter n:    "))
    y = n
    y += 1
    z = []
    for i in range(0, n + 1):
        y -= 1
        z.append(y)
    z.reverse()
    for i in z:
        exa(i)


main()
