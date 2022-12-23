#Write a program that will calculate the number of trailing zeros in a factorial of a given number.

def zeros(n):
    count = 0

    ##reduce by counting factors of five, for every 5 you get another trailing 0
    while n >= 5:
        n //= 5
        count += n
    return count