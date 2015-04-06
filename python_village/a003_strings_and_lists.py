#!/usr/bin/python

#Problem

#Given: A string s of length at most 200 letters and four integers a, b, c and d.

#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

import rosalib

def main():
    string = raw_input()
    a, b, c, d = rosalib.get_input_integers(4)
    if d > len(string):
        return

    print string[a:b+1], string[c:d+1]

if __name__ == '__main__':
    main()
