#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:46:28 2021

@author: sysad
"""

'''You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.'''

def likes(names):
    '''create a dictionary with each key value representing the no. of peoplw liking 
    the post'''
    n = len(names)
    Dict = {
        0 : 'no one likes it', 
        1 : '{} likes it',
        2 : '{} and {} like it',
        3 : '{}, {} and {} like it', 
        4 : '{}, {} and {X} others like it'}
    
    return Dict[min(4, n)].format(*names[:3], X = n -2)

name = ['Akshay', 'Chandan', 'Sawan' ,'Nikita', 'Aneesha']

print(likes(name))