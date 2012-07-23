#!/usr/bin/env python

import sys

cache = {}

def rec_fib(n):
	if n in cache:
		return cache[n]
	
	if n <= 2:
		return 1
	
	_fib = iter_fib(n-1) + iter_fib(n-2)
	cache[n] = _fib
	return _fib

def iter_fib(n):
	n0 = 1
	n1 = 1
	i = 1
	while i < n:
		tmp = n1
		n1 = n0 + n1
		n0 = tmp
		i += 1
	return n0


if __name__ == "__main__":
	if len(sys.argv) != 2:
		usg =  "usage: fib.py <n>\n"
		usg += "ex. ./fib.py 12 or\n"
		usg += "./fib.py 29"
		raise ValueError(usg)

	n = int(sys.argv[1])
	print rec_fib(n), iter_fib(n)
