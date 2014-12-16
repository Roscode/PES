#!/usr/bin/python
#-*- coding: utf-8 -*-
#Copyright 2014 Clint Valentine & Darren Roscoe


"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
def greatestprimefactor():
    n = 600851475143
    #start with lowest prime
    prime = 2
    #if prime^2 is less than n there is another prime factor
    while prime*prime < n:
        while n%prime==0:
            #pull prime factor out
            n = n/prime
        prime+=1
    print(n)
