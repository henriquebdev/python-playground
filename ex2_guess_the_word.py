'''

 Summary: The User needs to discover the hidden word. To do this, he can try as many times as necessary.
 He will only need to type to one word at time.

 1º condition: If the type word is correct, the system will show at console the length of the secrect
 word using stars(*) for the letters that yet not discovery and will show the correct position of the
word that the user got right.

 2º condition: If the word is wrong, the system will show at the console just de number of the length
 using starts. And then it will ask the user for another option.

 Obs: don't forgget the usually validations

 '''

loop_controller = False
secret_word = 'roses'

while loop_controller == False:
    chosen_word = input('Write the word: ')

    try:
        if not chosen_word.isalpha() or len(chosen_word) != 1:
            raise ValueError("The input must contain only letters. Please try again")

    except ValueError as e:
        print('Error: ', e)
        continue

    


