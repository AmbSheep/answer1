#!/usr/bin/env python3
import sys
import math
l = int(sys.argv[1])
w = int(sys.argv[2])
gcd = math.gcd(l, w)
print(gcd, 'x', gcd)

