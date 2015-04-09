#!/usr/bin/python

# Problem
# http://rosalind.info/problems/hamm/

def hamming_distance(a, b):
    return len(filter(lambda x: x[0] != x[1], zip(a, b)))


def main(filename):
    with open(filename) as f:
        strands = [x.strip() for x in f.readlines()]
        print hamming_distance(strands[0], strands[1])


def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

