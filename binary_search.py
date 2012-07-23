#!/usr/bin/env python

import sys

def bin_search(collect, target, left, right):
	#print "--------------"
	#print ">>> left %s, right %s " % (left, right)
	
	if left > right:
		return None

	# compute "mid-point"
	mid = ((right - left) / 2) + left
	#print ">>> mid %s " % mid
	if collect[mid] == target:
		return mid
	elif collect[mid] > target:
		return bin_search(collect, target, left, mid-1)
	else:
		return bin_search(collect, target, mid+1, right)

if __name__ == "__main__":
	l1 = (1, 2, 5, 9, 12, 14, 17)
	t1 = 1
	t2 = 5
	t3 = 12
	t4 = 4
	t5 = 19
	print l1
	print "-------------------"
	print t1, bin_search(l1, t1, 0, len(l1) - 1)
	print t2, bin_search(l1, t2, 0, len(l1) - 1)
	print t3, bin_search(l1, t3, 0, len(l1) - 1)
	print t4, bin_search(l1, t4, 0, len(l1) - 1)
	print t5, bin_search(l1, t5, 0, len(l1) - 1)
