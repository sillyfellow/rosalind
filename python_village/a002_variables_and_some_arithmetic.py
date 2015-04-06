#!/usr/bin/python

#Problem

#Given: Two positive integers a and b, each less than 1000.

#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

import rosalib

def hyopotenuse(a, b):
    return (a * a) + (b * b)

def main(limit):
    a, b = raw_input().split()
    if (not rosalib.is_integer(a)) or (not rosalib.is_integer(b)):
        return
    a = int(a)
    b = int(b)
    if a < limit and b < limit:
        print hyopotenuse(a, b)

if __name__ == '__main__':
    main(1000)

