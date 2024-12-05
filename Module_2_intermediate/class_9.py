#Generator express : They are funcionts that know how to pause in certain situations 
# Difference between generator and iterator:

'''
Iterator: This is an object that implements the iter() and next() methods, allowing u to access
its elements one at a time. It can be created manually or for iterables (such as lists and dictionaries)
using iter()

Generator: This is a special type of iterator created with functions that use yield instead of return.
It generates values on demand, pausing its execution and resuming from where it left off, saving memory. 

'''

list_example = [number for number in range(5)]
print(list_example )