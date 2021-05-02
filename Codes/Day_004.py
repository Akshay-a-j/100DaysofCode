#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:24:59 2021

@author: sysad
"""
"""What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []"""

def anagrams(word, words):
    ret_words =[]
    length = len(word)
    for i in range(len(words)):
        n = 0
        len_wordi= len(words[i])
        if length == len_wordi:
            for w2 in words[i]:
                if w2 in word:
                    n +=1
        for w3 in word:
            if w3 in words[i]:
                n = n
            else:
                n -=1
        if (n == length) & (n == len_wordi):
            ret_words.append(words[i])
    return ret_words

'''***********************Best_preactice***********************'''
def anagrams(word, words):
    return [item for item in words if sorted(item) == sorted(word)]