#do Comment

#Print words in console
print("Any words")

"""
Multi-line comment 
"""

# named argument (sep)
print(10, 12, sep=" ")

# \n (Return) and \n (breakLine)
print(10, 12, sep=" ", end='\n')

# Python is a strongly typed programming language 
# Dynamic typing: Python already knows the type of information we are passing..

#Data Type

#String: text type, inside ' x '
print('any text')

#int: any number without punctuation
print(48)

#float: any number without punctuation (.)
print(12.9, -8.1) 

#boolean: false or true
print(False, True)

#typeof: show the type value inside. Its a class type (call able)
print(type(12.))

#type convertion: int(), float(), str()
print(int("3")+1)

#Create Variable
var_test = "any value"

#ellipsis
var = ... #test ellipsis

#string formatting (f-strings): f'any text{}'
var = f'{var_test} test'
float_example_1 = 3.256
varTest = f'Please, enter the code for this id ({float_example_1:.2f}) '

#controls decimal places
float_example_2 = 7.256
var = f'{float_example_2:.2f}'

#.format(x,y,z) : Its a method in python used for format in order to make them more flexible

format_variable = "Any word"
format_example = 'this is a test case using format here {}'.format(format_variable)
print(format_example)

#input : Using input function to collect data
name_example = input("What's is your name? ")
print(f'your name is {name_example}')

#if, else, elif: structures that allow us decision making
var_in_out = input('Do you want "enter" or "exit"? ' )

if var_in_out == 'enter':
    print('You entered the system')
elif var_in_out == 'exit':
    print('You left the system')
else:
    print('Invalid value. Please try again')
