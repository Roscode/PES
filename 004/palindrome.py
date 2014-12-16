#!/usr/bin/python
#-*- coding: utf-8 -*-
#Copyright 2014 Clint Valentine & Darren Roscoe

"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers
"""

from __future__ import print_function

ANSWER = []

for i in xrange(1, 1000):
    for j in xrange(1, 1000):
        test = str(i * j)
        if test == test[::-1]:
            ANSWER.append(int(test))

print(max(ANSWER))
