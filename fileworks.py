#!/usr/bin/python

import fileinput
import json

def get_input():
    A = []

    for line in fileinput.input():
        line = line.strip('\n').split();
        A.append({'id': int(line[0]), 'x': int(line[1]), 'y': int(line[2])})

    return A

def write_output(A):
    name = fileinput.filename() + ".tour"
    f = open(name, "w")
    for i in range(len(A)):
        f.write(json.dumps(A[i])+"\n")
    f.close()
