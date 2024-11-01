# Here we will create a simple calculator system for apply the knowledgment learned so far
# First step - Create the input variables

menu_option = ...
any_error = "" #ok
calculation = ...
msg_result = ""
        

while menu_option != 'S':
    
    try:
        initial_message = print('\nWelcome to the calculator menu \n')
        number_1 = input('Enter the first number: ')
        number_2 = input('Enter the second number: ')
        operator = input('Choose one operador (+,-,*,/): ')

        conversion_float_number_1 = float(number_1)
        conversion_float_number_2 = float(number_2)        
    
    except:  
        any_error ='Some or both numbers are invalidate. Please, try again.'
        print(f'\n{any_error}')        
        continue
    
    if operator == '+':
        ... #sum
        calculation = conversion_float_number_1 + conversion_float_number_2
        msg_result = f'\nThe sum of {conversion_float_number_1} + {conversion_float_number_2} is: {calculation}\n'

    if operator == '-':
        ... #subtraction
        calculation = conversion_float_number_1 - conversion_float_number_2
        msg_result = f'\nThe subtraction of {conversion_float_number_1} - {conversion_float_number_2} is: {calculation}\n'

    if operator == '*':
        ... #multiplication
        calculation = conversion_float_number_1 * conversion_float_number_2
        msg_result = f'\nThe multiplication of {conversion_float_number_1} * {conversion_float_number_2} is: {calculation}\n'

    if operator == '/':
        ... #division
        calculation = conversion_float_number_1 / conversion_float_number_2
        msg_result = f'\nThe division of {conversion_float_number_1} / {conversion_float_number_2} is: {calculation}\n' 

    print(msg_result)

    menu_option = input('Do you want exit the calculator? [S/N]: ')
    
  