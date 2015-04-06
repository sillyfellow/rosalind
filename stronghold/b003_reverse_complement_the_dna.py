#!/usr/bin/python


#Problem

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

import rosalib

def dna_reverse_complement(s):
    complement = [rosalib.base_complement(c) for c in s.strip()]
    complement.reverse()
    return ''.join(complement)

def main(filename):
    with open(filename) as f:
        print dna_reverse_complement(f.read())

def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

