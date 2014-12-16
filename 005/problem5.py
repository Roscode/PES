#!/usr/bin/python
#-*- coding: utf-8 -*-
#Copyright 2014 Clint Valentine & Darren Roscoe


"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder. What is the smallest
positive number that is evenly divisible by all of the numbers from
1 to 20?
"""
divisors = range(1, 21)
donecheck = [0]*20
n = 20
cont = True
while cont:
    for i in divisors:
        if n%i==0:
            donecheck[i-1]=1
    if sum(donecheck) == 20:
        cont = False
    else:
        donecheck = [0]*20
        n+=20
print(n)
"""
print(n/2.0)
print(n/3.0)
print(n/4.0)
print(n/5.0)
print(n/6.0)
print(n/7.0)
print(n/8.0)
print(n/9.0)
print(n/10.0)
print(n/11.0)
print(n/12.0)
print(n/13.0)
print(n/14.0)
print(n/15.0)
print(n/16.0)
print(n/17.0)
print(n/18.0)
print(n/19.0)
print(n/20.0)
"""
