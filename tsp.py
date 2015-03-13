#!/usr/bin/env python

from fileworks import get_input
from fileworks import write_output
from fileworks import search
import math

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

distances = []
solution = []

for i in range(0,len(cities)):
	for j in range(i+1, len(cities)):
		dx = cities[j]['x'] - cities[i]['x']
		dy = cities[j]['y'] - cities[i]['y']
		distance = int(round(math.sqrt(dx*dx + dy*dy)))
		distances.append({'id1': cities[i]['id'], 'id2': cities[j]['id'], 'dist': distance})

		
solution.append(0) #distance is first item

firstPair = min(distances, key=lambda x:x['dist'])
nextCity = firstPair['id1']

for k in range(0,len(cities)-2):
	solution.append(nextCity)

	citysearch = search(nextCity, distances)

	minPair = min(citysearch, key=lambda x:x['dist'])
	solution[0] = solution[0] + minPair['dist']

	if minPair['id1'] == nextCity:
		temp = minPair['id2']
	else:
		temp = minPair['id1']
		
	#remove all pairs that include the most recent city, runs faster than searching through the entire list
	distances = [x for x in distances if not(nextCity == x.get('id1') or nextCity == x.get('id2'))]

	nextCity = temp


solution.append(nextCity)

#at this point, a single pair of cities is left in the distances list
if distances[0]['id1'] == nextCity:
	nextCity=distances[0]['id2']
else:
	nextCity=distances[0]['id1']


solution.append(nextCity)
solution[0] = solution[0] + distances[0]['dist']


dx = cities[firstPair['id1']]['x'] - cities[nextCity]['x']
dy = cities[firstPair['id1']]['y'] - cities[nextCity]['y']
distance = int(round(math.sqrt(dx*dx + dy*dy)))

solution[0] = solution[0] + distance


"""
This will output results to disk. Existing files are overwritten, not appended.

A is assumed to be an array where:
    A[0] = length of the tour
    A[1], A[2], ... A[n] = city identifier numbers in order they are visited

"""
write_output(solution)