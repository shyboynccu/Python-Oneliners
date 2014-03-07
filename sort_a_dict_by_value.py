#!/usr/bin/env python3

# test data
d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}

# One-liner to sort a dict by its value
print (sorted(d.items(), key = lambda x: x[1]))
