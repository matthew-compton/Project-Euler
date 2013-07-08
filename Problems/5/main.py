#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Ambergleam <ambergleam@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import math, prime

# The problem we're working on
problem = "5"

# Problem description
description = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Sum of all the terms
solution = 0

# Brute force method
def solveBruteForce(top):
	
	# Define the upper limit
	upperLimit = 1
	for i in xrange(1, top+1):
		upperLimit *= i
	#print upperLimit
	
	# Define the lower limit
	lowerLimit = 1
	for i in xrange(1, top+1):
		if (prime.isPrime(i) == True):
			lowerLimit *= i
	#print lowerLimit
	
	# Check between the limits
	for num in xrange(lowerLimit, upperLimit+1):
		flag = True
		for j in xrange(1, top+1):
			if (num % j != 0):
				flag = False
		if (flag == True):
			return num
	
	# Worst case scenario
	return upperLimit

# Solve the problem
def solve():
	global solution
	#solution = solveBruteForce(10)
	solution = solveBruteForce(20)

# Main function that just runs the solver
def main():
	print "Problem " + problem
	print description
	print "...\n"
	solve()
	print "\n...\n"
	print solution

# The actual main function for command line run
if __name__ == '__main__':
	main()
