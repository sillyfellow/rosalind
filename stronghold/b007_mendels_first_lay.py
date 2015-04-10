#!/usr/bin/python

# Problem
# http://rosalind.info/problems/iprb/

def recessive_chances(hetero_dom, homo_rec, total):
    hetero_dom, homo_rec, total = hetero_dom * 1.0, homo_rec * 1.0, total * 1.0
    both_rec = (homo_rec / total) * ((homo_rec - 1) / (total - 1))
    one_each = (homo_rec / total) * ((hetero_dom / 2) / (total - 1)) + ((hetero_dom / 2) / total) * (homo_rec / (total - 1))
    both_het = ((hetero_dom / 2) / total) * (((hetero_dom - 1) / 2) / (total - 1))
    return both_rec + one_each + both_het

def main(filename):
    with open(filename) as f:
        k, m, n = map(lambda x: int(x), f.readline().strip().split())
        recessive_prob = recessive_chances(m, n, k + m + n)
        dominant_prob = 1 - recessive_prob
        print dominant_prob, recessive_prob

def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

