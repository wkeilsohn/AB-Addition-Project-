# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:45:09 2018

@author: William Keilsohn
"""

# A + B Project
# Based off of: http://rosettacode.org/wiki/A%2BB

# Input packages
import pandas as pd

# Gather User Input

numbs = input("Please enter two numbers seperated by a space: ")

# Convert input to numbers (floats)
strings = numbs.split() #The space becomes it's own slot in the list.
strLis = list(strings) 

numLis =[]
for i in strLis:
  numLis.append(float(i)) #Just incase the user doesn't enter whole numbers

# Do the math
answer = numLis[0] + numLis[1]

# Print the result
print('\n') #Just makes the output look nicer  
print(answer)

# Now the problem demands a specific format, so here is a re-creation
inputs = str(numLis[0]) + ' and ' + str(numLis[1]) #Just looks a little nicer. Not really necessary.

data = {'Input' : inputs,
        'Output' : answer}
results = pd.DataFrame(data, index = ['']) #You "need" an index.
print('\n')
print(results)