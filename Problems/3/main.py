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
problem = "3"

# Problem description
description = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Sum of all the terms
solution = 0

# Finds all of the prime factors of a number
def getPrimeFactors(num):
	factors = []
	for i in reversed(xrange(num)):
		if (i != 0 and num % i == 0):
			if (prime.isPrime(i) == True):
				factors.append(i)
	return factors

# Finds the largest prime factor of a number
def largestPrimeFactor(num):
	global solution
	top = int(math.ceil(math.sqrt(num)))
	for i in range(2, top+1):
		if (num % i == 0):
			if (prime.isPrime(i) == True):
				solution = i

# Solve the problem
def solve():
	#solution = largestPrimeFactor(13195)
	#print getPrimeFactors(13195)
	solution = largestPrimeFactor(600851475143)
	#print getPrimeFactors(600851475143)

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
