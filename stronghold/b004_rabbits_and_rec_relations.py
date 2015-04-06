#!/usr/bin/python

#Problem
# http://rosalind.info/problems/fib/

import rosalib

def fibo_with_larger_litter_iter(n, k):
    a, b = 1, 1
    while n > 1:
        a = b + k * a
        b = a + k * b
        n = n - 2
    return b if n == 0 else a

def fibo_with_larger_litter_rec(n, k):
    if n <= 2:
        return 1
    return fibo_with_larger_litter_rec(n - 1, k) + k * fibo_with_larger_litter_rec(n - 2, k)

def main():
    a, b = rosalib.get_input_integers(2)
    print fibo_with_larger_litter_iter(a, b)
    print fibo_with_larger_litter_rec(a, b)

if __name__ == '__main__':
    main()

