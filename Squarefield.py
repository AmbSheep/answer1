#!/usr/bin/env python3
import sys
def gcd(a, b):
    while a != b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

if __name__=='__main__':
    print(gcd(int(sys.argv[1]), int(sys.argv[2])), 'x', gcd(int(sys.argv[1]), int(sys.argv[2])))

