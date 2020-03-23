"""
In this kata you have to create all permutations of an input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders.
The order of the permutations doesn't matter.
"""

import itertools
def permutations(string):
    return list(set(''.join(i) for i in itertools.permutations(string, len(string))))


