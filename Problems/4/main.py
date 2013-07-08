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

import math, palindrome

# The problem we're working on
problem = "4"

# Problem description
description = """
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Sum of all the terms
solution = 0

# Solve the problem
def solve():
	global solution
	for i in reversed(xrange(100, 1000)):
		for j in reversed(xrange(100, 1000)):
			num = i * j
			if (palindrome.isPalindrome(num) == True and num > solution):
				solution = num
	return

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
