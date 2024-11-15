#Sets in python

'''
The definition:
    Set() in python is an 'unordered' and 'duplicate-free' collection, used to store unique elements
    and perform efficient operations like union, intersection and difference.

When we use?

    1) To eliminate duplicates from a collection
    2) To check if ant item is present in a collection efficiently (set operations are faster than lists)
    3) To perform mathematical operations such as union, intersection and difference.

Common set functions and methods:

    1) Create a set ('conjuto'):
        s = set([1,2,3])

    2) Add elements:
        s.add(4)
        console: {1,2,3,4}

    3) Remove elements:
        s.remove(2)
        console: {1,3,4}

    4) Check if an element is present:
        print(3 in s) console: True

    5) Union, intersection, difference and symmetric difference

        A = {1,2}
        B = {2,3}

        print (A | B) # Union: {1,2,3}
        print (A & B) # Intersection: {2}
        print (A - B) # Difference : {1}
        print (A ^ B) # Symmetric differente: {1,3}
            The symmetric, it includes all items that are unique to each set, excluding elements that
            are present in both
'''

a = {1,2}
b = {2,3}

print (a ^ b)
