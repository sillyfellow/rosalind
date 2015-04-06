#!/usr/bin/python

#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

def main(filename):
    with open(filename) as f:
        print f.read().replace('T', 'U').replace('t', 'u')


def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

