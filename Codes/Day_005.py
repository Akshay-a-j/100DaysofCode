#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:20:48 2021

@author: sysad
Credit:https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
"""
'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" '''


def duplicate_encode(word):
    word = list(word.lower())
    n = []
    for w in word: 
        n.append(word.count(w))
    for i in range(0,len(n)):
        if n[i] == 1:
            word[i] = '('
        else:
            word[i] = ')'
    return "".join(word)

'''************Best_Praectice******************'''
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])