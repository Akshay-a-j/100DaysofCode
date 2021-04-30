#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:04:06 2021

@author: sysad
"""

'''Jaden Smith, the son of Will Smith, is the star of films such as 
The Karate Kid (2010) and After Earth (2013). Jaden is also known for 
some of his philosophy that he delivers via Twitter. When writing on Twitter, 
he is known for almost always capitalizing every word. For simplicity, you'll 
have to capitalize each word, check out how contractions are expected to be 
in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. 
strings are actual quotes from Jaden Smith, but they are not capitalized in 
the same way he originally typed them.

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real " '''

def to_jaden_case(string):
    print(string)
    string = list(string)
    for i in range(len(string)):
        if string[0].islower():
            string[i]= string[i].capitalize()
        elif string[i] == ' ':
            string[i+1]= string[i+1].capitalize() 
    #print(string)
    return "".join(string)

def to_jaden_case(string):
    return " ".join(x.capitalize() for x in string.split())


string = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(string))
