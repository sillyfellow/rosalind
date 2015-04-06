#!/usr/bin/python

#Problem

#Given: A file containing at most 1000 lines.

#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.


def main(filename):
    f = open(filename, 'r')
    g = open(filename + '.out', 'w+')
    even = False
    for line in f.readlines():
        if even:
            g.write(line)
            print line,
        even = not even
    f.close()
    g.close()

def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

