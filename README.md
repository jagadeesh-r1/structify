# Intersections.py
This Python script counts the number of intersections between chords in a circle.

## Logic
The main logic is in the function `count_overlapping_lines`.
Here, we dont need the actual values of the point rather we need the sequence of the points which is 2nd tuple in the input. We separate the input into points and identifiers(name of the points) lists and use the identifiers list.
here, we can calculate the intersections based on a simple logic (Interleaving Points)[https://math.stackexchange.com/questions/735169/condition-for-intersection-of-chords-inside-a-circle]

In the `count_overlapping_lines`, we initialize a set which is implemented using hash tables in python makes the time complexity : O(1)

In the identifiers list we iterate over the points(from here ids will be referred as points/point). 
- If the point is a starting point, we add it to set.
- If its an ending point, count will be increased by the number of elements in the set -1(taking the 1st starting point added out of consideration) and we remove the element from set
- return the count.

## Time Complexity
The time complexity is `O(n)` as it would only iterate over the points only once.

## Input:
The input string should represent a series of lines, with each line represented by a tuple of points and identifiers. 
For example: (0.78, 1.47, 1.77, 3.92), (s1, s2, e1, e2)
Output:
Number of intersections: $intersections

## How to Run
To run the script, simply execute it with Python and paste the input string when prompted:

```python3 intersections.py```

## Prerequisites
Python 3.6 or later