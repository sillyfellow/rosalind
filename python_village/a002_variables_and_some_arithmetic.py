#!/usr/bin/python

#Problem

#Given: Two positive integers a and b, each less than 1000.

#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.


def hyopotenuse(a, b):
    return (a * a) + (b * b)

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main(limit):
    a, b = raw_input().split()
    if (not is_integer(a)) or (not is_integer(b)):
        return
    a = int(a)
    b = int(b)
    if a < limit and b < limit:
        print hyopotenuse(a, b)

if __name__ == '__main__':
    main(1000)

