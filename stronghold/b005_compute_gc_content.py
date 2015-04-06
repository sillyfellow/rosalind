#!/usr/bin/python

#Problem
#http://rosalind.info/problems/gc/

def gc_count(s):
    return len(filter(lambda x: x.upper() == 'G' or x.upper() == 'C', s))

def gc_content(s):
    return 100.0 * (1.0 * gc_count(s)) / (1.0 * len(s))

def fasta_gc_contents(fasta_sequence_pairs):
    return [(f, gc_content(s)) for f, s in fasta_sequence_pairs.iteritems()]

def main(filename):
    with open(filename) as f:
        fspairs = {}
        current_key = ''
        collected_sequences = []
        for line in f.readlines():
            if line[0] == '>':
                if current_key:
                    fspairs[current_key] = ''.join(collected_sequences)
                current_key = line.strip()
                collected_sequences = []
                continue
            collected_sequences.append(line.strip())
        ##lines = iter(f.readlines())
        ##fspairs = dict([(x.strip(), next(lines).strip()) for x in lines])
        #print fspairs.values()
        fgcpairs = fasta_gc_contents(fspairs)
        #print fgcpairs
        most_gc_contented = sorted(fgcpairs, key=lambda x: x[1])[-1]
        print most_gc_contented[0]
        print most_gc_contented[1]








def Usage(name):
    print "Usage: %s <filename>" % name

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        Usage(sys.argv[0])
    else:
        main(sys.argv[1])

