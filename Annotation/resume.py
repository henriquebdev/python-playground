'''
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
var1 = "any value"

#ellipsis
var3 = ... #test ellipsis

#string formatting (f-strings): f'any text{}'
var2 = f'{var1} test'
float_example_1 = 3.256
var4 = f'Please, enter the code for this id ({float_example_1:.2f}) '

#controls decimal places
var6 = 7.256
var5 = f'{var6:.2f}'

#.format(x,y,z) : Its a method in python used for format in order to make them more flexible

var7 = "Any word"
var8 = 'this is a test case using format here {}'.format(var7)
print(var8)

#input : Using input function to collect data
var9 = input("What's is your name? ")
print(f'your name is {var9}')

#if, else, elif: structures that allow us decision making
var10 = input('Do you want "enter" or "exit"? ' )

if var10 == 'enter':
    print('You entered the system')
elif var10 == 'exit':
    print('You left the system')
else:
    print('Invalid value. Please try again')


#Comparion operators: >, >=, <, <=, == and !=


v11 = 24
if v11<=10:
    print("Is bigger")
else:
    print("Is smaller")

#Logical operators : and, or, not

# Operators in, not in

var12 = 'world'
print('w' in 'world')

# len : Returns number of items

var13 = 'Python'
print(len(var13))
print(var13[0:4])

# try / except

var14 = '21'

try:
    ...
    if(var14>10):
        print("value grater than 10")
    else:
        print("value less than 0")
except:
    ...
    print("Except: Invalid Information")

# Constant

THIS_IS_CONSTANT = "constant has a default value"

'''

# while 

var_condition = True

while var_condition:
    print(1)
    print(2)
    var_condition = False
    
    break

# assignment operators (=, +=, -=, *=, /=. //=, **=, %=)

#.lower()  : Returns lowercase letters

# .startwith("x") : Returns if the initial letter is ""