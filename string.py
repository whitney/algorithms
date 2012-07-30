#!/usr/bin/env python

import sys

def reverse(string):
	length = len(string)
	chars = list(string)
	for i in range(length/2):
		tmp = chars[i]
		chars[i] = chars[length-1-i]
		chars[length-1-i] = tmp
	return "".join(chars)

def rev_sub_vector(v, l, r):
	i = l
	j = 0
	while i <= (l+r)/2: 
		tmp = v[i]
		v[i] = v[r-j]
		v[r-j] = tmp
		i += 1
		j += 1
	#for i in range(l, ((r+l)/2)+1):
	#	tmp = v[i]
	#	v[i] = v[r-i]
	#	v[r-i] = tmp
	#	i += 1
	return v

# rotate the elements of a vector
# i units to the left
def rotate(v, i):
	# reverse full vector
	rev_sub_vector(v, 0, len(v)-1)
	# reverse elems in [0, len(v)-i-1]
	rev_sub_vector(v, 0, len(v)-i-1)
	# reverse elems in [len(v)-i, len(v)-1]
	rev_sub_vector(v, len(v)-i, len(v)-1)
	return v

if __name__ == "__main__":
	s1 = ""
	s2 = "w"
	s3 = "wz"
	s4 = "wrz"
	s5 = "Whitney Zoller"
	print s1, reverse(s1)
	print s2, reverse(s2)
	print s3, reverse(s3)
	print s4, reverse(s4)
	print s5, reverse(s5)
	print "------------------"
	v1 = [1, 2, 3, 4, 5, 6]
	l1 = 0
	r1 = 2
	print v1
	rev_sub_vector(v1, l1, r1)
	print v1
	print "------------------"
	v1 = [1, 2, 3, 4, 5, 6]
	l1 = 0
	r1 = 5
	print v1
	rev_sub_vector(v1, l1, r1)
	print v1
	print "------------------"
	print "ROTATE (left 3 units)!"
	v0 = ["a", "b", "c", "d", "e", "f", "g", "h"]
	v1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
	v2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
	print "original vector: ", v0
	print "rev_sub_vector [0,4]:", rev_sub_vector(v0, 0, 4)
	print "rev_sub_vector [5,7]:", rev_sub_vector(v1, 5, 7)
	print "full rotate:", rotate(v2, 3)

