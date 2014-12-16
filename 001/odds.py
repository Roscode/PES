#!/usr/bin/python
#-*- coding: utf-8 -*-
#Copyright 2014 Clint Valentine & Darren Roscoe

"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import print_function

ANSWER = 0

for x in xrange(1000):
    if x != 0 and (x % 3 == 0 or x % 5 == 0):
        ANSWER += x

print(ANSWER)
