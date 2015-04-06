#!/usr/bin/python

#Problem

#Given: Two positive integers a and b, each less than 1000.

#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

import rosalib

def main(limit):
    a, b = rosalib.get_input_integers(2)
    if a < limit and b < limit:
        print rosalib.hyopotenuse(a, b)

if __name__ == '__main__':
    main(1000)

