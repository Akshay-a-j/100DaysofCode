'''source:https://www.codewars.com/kata/541c8630095125aba6000c00/solutions/python'''
"""Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in
this way until a single-digit number is produced. 
The input will be a non-negative integer."""

def digital_root(n):
    if len(str(n))>1:
        while len(str(n))>1:
            global summ
            summ = 0
            for i in range(len(str(n))):
                summ += n//(10**(len(str(n))-1))
                n = n%(10**(len(str(n))-1))
            n = summ
    else:
        summ = n
    return int(summ)


'''map() function returns a map object(which is an iterator) of 
the results after applying the given function to each item of a 
given iterable (list, tuple etc.)'''

def digital_root(n):
    # ...
    while len(str(n))>1:
        n=sum(map(int,str(n)))
    return n
print(digital_root(56))
