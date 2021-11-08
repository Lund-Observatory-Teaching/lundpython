#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:39:32 2021

@author: Simon
"""
@profile
def sieve(n):
    primes=[]
    test=list(range(3,n+1, 2) )
    while test[0]<=n**0.5:
        p = test.pop(0) 
        primes.append(p)
        test = [n for n in test if n%p] #Overwrite test each loop
    return primes+test

primes = sieve(5000)
print(len(primes))