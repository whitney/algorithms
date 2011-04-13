#!/usr/bin/env python

###############################################
# http://people.csail.mit.edu/bdean/6.046/dp/ #
###############################################

# 1: Maximum Value Contiguous Subsequence
# Given a sequence of n real numbers A(1) ... A(n), 
# determine a contiguous subsequence A(i) ... A(j) 
# for which the sum of elements in the subsequence is maximized.
class MaxValContSub:
	"""
	--- subproblem: given an array A of n real numbers all we can define a function m
	such that for j in 0, 2, ..., n-1 m(j) is equal to the the maximum sum of elements
	of the subset ENDING WITH j.

	As such we have a recursive definition of m: m(j) = max(m(j-1) + A[j], A[j]), 
	which says that the max sum at element j is either the max sum of the sequence ending 
	at the previous element (ie we're adding to the previous subsequence) OR 
	it is the element A[j] itself (ie we're starting a new subsequence)   
	"""

	def solve(self, array):
		curr_sub     = [array[0]]
		subs         = [curr_sub]
		original     = []
		curr_max     = 0
		curr_max_idx = 0

		for i in range(len(array)):
			original.append(array[i])
			if i > 0:
				if array[i - 1] + array[i] >= array[i]:
					# current sequence continues
					array[i] = array[i - 1] + array[i]
					if array[i] >= array[i-1]:
						curr_sub.append(original[i])
					else:
						curr_sub = [original[i]]
				else:
					# new sequence begins
					curr_sub = [original[i]]
				subs.append(curr_sub)
			if array[i] >= curr_max:
				curr_max = array[i]
				curr_max_idx = i
		#return array, subs
		return curr_max, subs[curr_max_idx]

	def test(self):
		array = [1, 2, -30, 4, 5, -22, 3, 4, 5]
		print "testing on input: {0}".format(array)
		print "output (subsequence max, subsequence): {0}".format(self.solve(array))

# 2: Making Change
# Given a list of N coins, their values (V1, V2, ... , Vn),
# and the total sum S. Find the minimum number of coins the sum of which is S 
# (we can use as many coins of one type as we want), 
# or report that it's not possible to select coins in such a way that they sum up to S. 
class MakingChange:
	"""
	--- subproblem: for any i in 1, 2, ..., S, we try to find the minimum number of coins 
	from the collection such that the sum would be i. Note then that we have a recursive definition 
	of s: 

	// initialize
	for i = 1, 2, ..., S:
		min[i] = infinity
	// it takes 0 coins to sum to S = 0
	min[0] = 0
	for i = 1, 2, ..., S:
		for v = V1, V2, ..., Vn:
			if i >= v and min[i-v] + 1 < min[i]:
				min[i] = min[i-v] + 1 
	"""

	def solve(self, coin_vals, S):
		min = {0: 0}
		inf = float('inf')

		for i in range(1, S+1):
			for v in coin_vals:
				if i >= v and min.get(i-v, inf) + 1 < min.get(i, inf):
					min[i] = min.get(i-v, inf) + 1
		return min.get(S, inf)

	def test(self):
		S = 99
		coin_vals = [1, 5, 10, 25, 50]
		print "testing on input (S, coin_vals): {0}, {1}".format(S, coin_vals)
		print "output: {0}".format(self.solve(coin_vals, S))

# 3: Longest Increasing Subsequence
# Given a sequence of n real numbers A(1) ... A(n),
# determine a subsequence (not necessarily contiguous) of maximum length 
# in which the values in the subsequence form a strictly increasing sequence. 
class LongIncSub:
	"""
	--- subproblem: we define two subproblems that will help us to solve this. For i in 
	1, 2, ..., n let s(i) denote the length of the longest strictly increasing (not necessarily
	contiguous) subsequence of A ending at or before A[i]. Additionally let m(i) be the largest 
	element in the LONGEST subset of A ending at or before A[i].

	//initialize
	for i = 1, 2, ..., n:
		s[i] = 1 // the default length of a subsequence is 1
		m[i] = A[i] // the default max value of a subsequence is the element 
	m[0] = A[0]
	s[0] = 1
	for i = 1, 2, ..., n:
		// m:
		if A[i] > m[i-1]:
			m[i] = A[i]
			s[i] = s[i-1] + 1
		elif (A[i] > A[i-1]) and (m[i-1] == 1):
			s[i] = s[i-1] + 1
		else:
			m[i] = m[i-1]
			s[i] = s[i-1]

	* TODO: find the actual sequence, not just the length
	"""

	def solve(self, array):
		s = {0: 1}
		m = {0: array[0]}
		for i in range(1, len(array)):
			s[i] = 1
			m[i] = array[i]
			if array[i] > m[i-1]:
				m[i] = array[i]
				s[i] = s[i-1] + 1
			elif (array[i] > array[i-1]) and (m[i-1] == 1):
				s[i] = s[i-1] + 1
			else:
				m[i] = m[i-1]	
				s[i] = s[i-1]	
		return s, m

	def test(self):
		reals = [1, -5, 1, 1, 1, 1, -4, 2, 3, 4, 25, 50, -2, -32, 8, 9]
		s, m = self.solve(reals)
		print "testing on input: {0}".format(reals)
		print "length (s):       {0}".format(s)
		print "largest (m):      {0}".format(m)
		print "max s:            {0}".format(sorted(s.values())[-1])

# 4: Box Stacking
# You are given a set of n types of rectangular 3-D boxes, 
# where the i^th box has height h(i), width w(i) and depth d(i) (all real numbers). 
# You want to create a stack of boxes which is as tall as possible, 
# but you can only stack a box on top of another box if the dimensions of 
# the 2-D base of the lower box are each strictly larger than those of 
# the 2-D base of the higher box. 
# Of course, you can rotate a box so that any side functions as its base. 
# It is also allowable to use multiple instances of the same type of box.
class BoxStacking:
	"""
	Note, in order to simplify things such that we can ignore the rotational issues,
	we define a helper method to compute the rotational permutations of the cuses such that for a cube
	have dimensions [height=h, width=w, depth=d], we get three boxes: [h, w, d], [w, h, d], [d, w, h].
	Also observe that for any width and depth we can assume--without loss of generality--that 
	width >= depth.

	--- subproblem: for j in range of sorted-by-decreasing-base-area permuted-cubes, 
	let h(j) denote the maximal height of a tower where the jth cube is the final block on tower.
	So we define h(j) recursively as follows: for i < j, h(j) := max{h(i)} + height(jth cube)
	"""

	def solve(self, cubes):
		# compute rotational permutations
		cubes = self.rotational_permutes(cubes)
		# sort by base area, decreasing
		cubes = sorted(cubes, cmp=lambda a, b: (b[1]*b[2]) - (a[1]*a[2]))
		curr_max_idx = 0
		h = {0: cubes[0][0]}
		for i in range(1, len(cubes)):
			if cubes[curr_max_idx][1] > cubes[i][1] and cubes[curr_max_idx][2] > cubes[i][2]:
				h[i] = max(h.values()) + cubes[i][0]
			else:
				h[i] = cubes[i][0]

			if h[i] > h[curr_max_idx]:
				curr_max_idx = i
					
		return max(h.values())

	def rotational_permutes(self, cubes):
		permutes = []
		for cube in cubes:
			h, w, d = cube[0], cube[1], cube[2]
			permutes.extend([[h, w, d], [w, h, d], [d, w, h]])
		return permutes

	def test(self):
		# cube = [heght, width, depth]
		cubes = [
				[1, 3, 3], [4, 3, 2], [5, 1, 1],
				[3, 4, 2], [3, 3, 3], [2, 8, 4],
				[4, 2, 2], [6, 1, 1], [1, 4, 1]
				]
		return self.solve(cubes)

# 5: Building Bridges
# Consider a 2-D map with a horizontal river passing through its center. 
# There are n cities on the southern bank with x-coordinates a(1) ... a(n) 
# and n cities on the northern bank with x-coordinates b(1) ... b(n). 
# You want to connect as many north-south pairs of cities as possible 
# with bridges such that no two bridges cross. When connecting cities, 
# you can only connect city i on the northern bank to city i on the southern bank. 
class Bridges:
	"""
	--- subproblem:
	"""

	def solve(self, cubes):
		pass

	def test(self):
		pass

# 6: Integer Knapsack Problem (Duplicate Items Forbidden)
# This is the same problem as the example above, except here 
# it is forbidden to use more than one instance of each type of item.
#class IntKnapsack:
#	"""
#	--- subproblem:
#	"""
#	pass

# 7: Balanced Partition
# You have a set of n integers each in the range 0 ... K. 
# Partition these integers into two subsets such that you minimize |S1 - S2|, 
# where S1 and S2 denote the sums of the elements in each of the two subsets.
#class BalPartition:
#	"""
#	--- subproblem:
#	"""
#	pass

# 8: Edit Distance
# Given two text strings A of length n and B of length m, you want to transform A into B 
# with a minimum number of operations of the following types: 
# delete a character from A, insert a character into A, or change some character in A into a new character. 
# The minimal number of such operations required to transform A into B is called the edit distance between A and B.
class EditDistance:
	"""
	--- subproblem: 
	"""

	def levenshtein(self, source, target):
		d = {}
		s = len(source) + 1
		t = len(target) + 1

		for i in range(s):
			d[i, 0] = i # the distance of any source string to an empty target string

		for j in range(t):
			d[0, j] = j # the distance of any target string to an empty source string

		for j in range(1, t):
			for i in range(1, s):
				if source[i] == target[j]:
					d[i, j] = d[i-1, j-1]
				else:
					d[i, j] = min(
								d[i-1, j] + 1, # immediately above
								d[i, j-1] + 1, # immediately to the left
								d[i-1, j-1] + 1  # above and to the left
								)
		return d[s-1, t-1]

	def test(self):
		pass

# 9: Counting Boolean Parenthesizations
# You are given a boolean expression consisting of a string of the symbols 
# 'true', 'false', 'and', 'or', and 'xor'. Count the number of ways to parenthesize the expression 
# such that it will evaluate to true. For example, there is only 1 way to parenthesize 'true and false xor true' 
# such that it evaluates to true.
#class BooleanParens:
#	"""
#	--- subproblem:
#	"""
#	pass

# 10: Optimal Strategy for a Game
# Consider a row of n coins of values v(1) ... v(n), where n is even. 
# We play a game against an opponent by alternating turns. In each turn, 
# a player selects either the first or last coin from the row, 
# removes it from the row permanently, and receives the value of the coin. 
# Determine the maximum possible amount of money we can definitely win if we move first.
#class GameStrategy:
#	"""
#	--- subproblem:
#	"""
#	pass

# 11: Two-Person Traversal of a Sequence of Cities
# Two-Person Traversal of a Sequence of Cities. You are given an ordered sequence of n cities, 
# and the distances between every pair of cities. You must partition the cities into two subsequences 
# (not necessarily contiguous) such that person A visits all cities in the first subsequence (in order), 
# person B visits all cities in the second subsequence (in order), 
# and such that the sum of the total distances travelled by A and B is minimized. 
# Assume that person A and person B start initially at the first city in their respective subsequences.
#class CityTraversal:
#	--- subproblem:
#		"""
#	"""
#	pass

# 12: Bin Packing
# in Packing (Simplified Version). You have n1 items of size s1, n2 items of size s2, and n3 items of size s3. 
# You'd like to pack all of these items into bins each of capacity C, 
# such that the total number of bins used is minimized.
#class BinPacking:
#	"""
#	--- subproblem:
#	"""
#	pass

