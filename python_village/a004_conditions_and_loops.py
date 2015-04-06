#!/usr/bin/python

#Problem

#Given: Two positive integers a and b (a<b<10000).

#Return: The sum of all odd integers from a through b, inclusively.

import rosalib

def main(limit):
    a, b = rosalib.get_input_integers(2)
    if (a >= limit) or (b >= limit):
        raise "We do not handle beyond limit: %d" % limit
    next_odd = a if (a % 2 == 1) else a + 1
    print sum(xrange(next_odd, b + 1, 2))

if __name__ == '__main__':
    main(10000)
