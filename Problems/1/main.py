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

# The problem we're working on
problem = "1"

# Problem description
description = """
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# solve the problem
def solve():
	solution = 0
	for i in range(1, 1000):
		if (i % 3 == 0 or i % 5 == 0):
			#print i
			solution += i
	return solution

# Main function that just runs the solver
def main():
	print "Problem " + problem
	print description
	print "...\n"
	solution = solve()
	print solution
	return 0

# The actual main function for command line run
if __name__ == '__main__':
	main()
