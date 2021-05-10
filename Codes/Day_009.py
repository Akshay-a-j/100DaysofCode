#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:38:28 2021

@author: sysad
credit:https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
"""

'''Write a function that takes an integer as input, and returns the number of 
bits that are equal to one in the binary representation of that number. You can 
guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function 
hould return 5 in this case'''

def count_bits(n):
    x = 0
    while n >= 1:
        x +=(n%2)
        n = n//2
    return x