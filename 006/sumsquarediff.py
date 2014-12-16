#!/usr/bin/python
#-*- coding: utf-8 -*-
#Copyright 2014 Clint Valentine & Darren Roscoe

"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

from __future__ import print_function

print(sum([x for x in xrange(1, 101)])**2 -
      sum([x**2 for x in xrange(1, 101)]))
