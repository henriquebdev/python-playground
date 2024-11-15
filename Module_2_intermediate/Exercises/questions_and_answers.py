questions = [
    {
        'Question': 'what is 2+2?',
        'Options': ['1','3','4','5'],
        'Response': '4'
    },
    {
        'Question': 'what is 5*5?',
        'Options': ['25','55','10','51'],
        'Response': '25'
    }  
  
]
score = 0

for question in questions:
    print(f'Question: {question['Question']}')
    print('\nOptions\n')
    i = 0    
    for option in question['Options']:
         print(f'{i}) {option}')
         i+=1
    response = input('\nChoose an option: ')
    format_response = int(response)
    try:        
         if((question['Options'][format_response]) == question['Response']):
              response_calc = 'Got it ✔️\n'
              score+=1
         else:
              response_calc = 'Wrong ❌\n'
                    
    except:
         print('Wrong ❌\n') 
         continue       
    
    print(response_calc)

print(f'You got {score} out of {len(questions)} questions right\n')
