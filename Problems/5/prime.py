#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prime.py
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

import unittest, math

# Determines if a given number is prime
def isPrime(num):
	# One is not a prime
	if (num == 1):
		return False
	# Two is a prime
	if (num == 2):
		return True
	# Otherwise check
	top = int(math.ceil(math.sqrt(num)))
	for i in range(2, top+1):
		if (num % i == 0):
			return False
	return True

# Unit test class for isPrime
class testIsPrime(unittest.TestCase):
	
	def test_primes(self):
		nums = [2,3,5,7,11,13,17,19]
		flag = True
		for num in nums:
			if (isPrime(num) != True):
				flag = False
		self.failUnless(flag == True)
		
	def test_nonprimes(self):
		nums = [1,4,6,8,9,10,12,14,15,16,18,20]
		flag = True
		for num in nums:
			if (isPrime(num) != False):
				flag = False
		self.failUnless(flag == True)

def main():
	unittest.main()

if __name__ == '__main__':
	main()

