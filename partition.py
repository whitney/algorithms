#!/usr/bin/env python

import sys
import math

"""
This analytic solution uses the fact 
that the output is equal to the upper 
bound of the input divded by 10.

So for inputs within the window [5001,10000], 
the upper bound is 10000 and the output is
10000/10 = 1000.

The "upper bound" is discovered by computing 
the log base-10 of n--call this value l--then determining 
which of the following is the smallest upper bound
of n: [10, 10^l, 5*(10^l), 10*(10^l)].
"""

SCAL_QUOTIENT = 10

def main(n):
	if n < 1:
		raise ValueError("Input must be an int >= 1.")

	upperBound0 = 10
	upperBound1 = pow(10,int(math.log10(n)))
	upperBound2 = 5*upperBound1

	if n <= upperBound0:
		# n in [1, 10]
		return upperBound0/SCAL_QUOTIENT
	elif n <= upperBound1:
		# n in [11, 10^l]
		return upperBound1/SCAL_QUOTIENT
	elif n <= upperBound2:
		# n in (10^l, 5*10^l]
		return upperBound2/SCAL_QUOTIENT
	else:
		# n in (5*10^l, 10*10^l]
		return upperBound1

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usg =  "usage: partition.py <n>\n"
		usg += "ex. ./partition.py 12 or\n"
		usg += "./partition.py 29"
		print usg
		sys.exit(1)

	n = int(sys.argv[1])
	try:
		print main(n)
	except ValueError as e:
		print e
		sys.exit(1)
