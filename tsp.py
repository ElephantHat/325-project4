#!/usr/bin/env python

from fileworks import get_input
from fileworks import write_output

'''
This will read the input file into an array of objects with this format:

    [{'id': 0, 'x': 1, 'y': 2},...]

id = city's identifier number
x = city's x-coordinate
y = city's y-coordinate
All 3 are integers


So, to access the 5th city's info would be:
    someVariable = cities[4]['<id|x|y>']
(remember, lists are zero-indexed)
'''
cities = get_input()



"""
This will output results to disk. Existing files are overwritten, not appended.

A is assumed to be an array where:
    A[0] = length of the tour
    A[1], A[2], ... A[n] = city identifier numbers in order they are visited

"""
write_output(A)
