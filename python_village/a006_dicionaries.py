#!/usr/bin/python


#Problem

#Given: A string s of length at most 10000 letters.

#Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.


import rosalib

def main(filename):
    d = {}
    f = open(filename, 'r')
    for line in f.readlines():
        for word in line.split():
            d[word] = d.get(word, 0) + 1
    f.close()
    rosalib.print_dict(d)

def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

