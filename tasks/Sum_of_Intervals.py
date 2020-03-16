"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
"""

def sum_intervals(arr):
    s = set()
    for a, b in arr:
        for elem in range(a, b):
            s.add(elem)
    return len(s)