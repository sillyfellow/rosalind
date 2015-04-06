#!/usr/bin/python

#Problem

#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


#import rosalib

def count_dna_nucleotides(string):
    d = {}
    for base in string:
        d[base] = 1 + d.get(base, 0)
    return d

def print_nucleotide_count(d):
    for b in 'ACGT':
        print d.get(b, '0'),

def main(filename):
    with open(filename) as f:
        d = count_dna_nucleotides(f.read())
        print_nucleotide_count(d)


def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

