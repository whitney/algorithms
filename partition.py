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
the log base-10 of n, then calculating the 
values referred to as tenCeil and fiveCeil.
tenCeil values are of the form 10^p, fiveCeil 
values are of the form 5*tenCeil.

tenCeil and fiveCeil are the potential upper
bounds of the input n. Since tenCeil is the 
smaller upper bound, if n <= tenCeil, then 
tenCeil is considered the true upper bound. 
If tenCeil is not the upper bound we check if 
fiveCeil is. If fiveCeil is not the upper 
bound for n (ie the fiveCeil for n = 501 is 500) 
then the output is equal to tenCeil (which in 
this case is 10^2=100).
"""

def mainBak(n):
	# How many "tens" are in this number?
	# The number of tens in a number n is 
	# defined as the number t such that 
	# n = 10^t + a, where 10^(t+1) > n. 
	tens = int(math.floor(math.log10(n)))
	print ">>> tens: %s" % tens

	if tens == 0:
		return 1

	tenCeil = pow(10,tens)
	if n <= tenCeil:
		return tenCeil/10

	fiveCeil = 5*tenCeil
	if n <= fiveCeil:
		return fiveCeil/10

	return tenCeil

def main(n):
	if n < 1:
		raise ValueError("Input must be an int >= 1.")

	smallUpperBound = pow(10,int(math.floor(math.log10(n))))
	if tens == 0:
		upperBound = 10
	elif n <= smallUpperBound:
		upperBound = smallUpperBound
	elif n <= 5*smallUpperBound:
		upperBound = 5*smallUpperBound
	else:
		upperBound = 10*smallUpperBound
	return upperBound/10

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
