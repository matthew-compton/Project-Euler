#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  palindrome.py
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

import unittest

# Determines if a given number is a palindrome
def isPalindrome(num):
	string = str(num)
	for i in range(0, len(string)/2):
		if (string[i] != string[len(string)-i-1]):
			return False
	return True

# Unit test class for isPrime
class testIsPalindrome(unittest.TestCase):
	
	def test_palindromes(self):
		nums = [1001,2112,5445,7777,1331]
		flag = True
		for num in nums:
			if (isPalindrome(num) != True):
				flag = False
		self.failUnless(flag == True)
		
	def test_nonpalindromes(self):
		nums = [1234,4355,5553,6622,1888]
		flag = True
		for num in nums:
			if (isPalindrome(num) != False):
				flag = False
		self.failUnless(flag == True)

def main():
	unittest.main()

if __name__ == '__main__':
	main()

