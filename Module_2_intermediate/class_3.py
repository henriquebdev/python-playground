
#Closure (Is an inner function that captures and 'remembers' variables from its defining environment)
def create_greeting(greeting, name):
    def greet():
        return f'{greeting},{name}'
    return greet

ex_1 = create_greeting('Good morning', 'Luiz')
print(ex_1())

def creates_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

result_multiplier = creates_multiplier(2)
print(result_multiplier(3))