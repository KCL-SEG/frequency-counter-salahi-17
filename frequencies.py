"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in range(len(items)):
	    items[x] = str(items[x])
    for x in range(len(items)):
        item = items[x]
        count = 0
        for each in items:
            if each == item:
                count += 1
        frequencies[item] = count
    # Your code goes here
    return frequencies



