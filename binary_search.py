#!/usr/bin/env python

import sys

def bsearch(collect, target):
	l = 0
	r = len(collect)-1
	while l <= r:
		m = (l+r)/2
		if target == collect[m]:
			return m
		elif target < collect[m]:
			r = m-1
		else:
			l = m+1
	return -1

if __name__ == "__main__":
	l1 = (1, 2, 5, 9, 12, 14, 17)
	t1 = 1
	t2 = 5
	t3 = 12
	t4 = 4
	t5 = 19
	print l1
	print "-------------------"
	print t1, bsearch(l1, t1)
	print t2, bsearch(l1, t2)
	print t3, bsearch(l1, t3)
	print t4, bsearch(l1, t4)
	print t5, bsearch(l1, t5)
