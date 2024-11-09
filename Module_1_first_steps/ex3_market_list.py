'''

 Summary: Create a market list where the user must have the possibility to (insert, delete(using index)
 and list)

 Obs: don't forgget the usually validations

 '''

array_marlet_list=[]
loop_controller = False

while loop_controller == False:
    chosen_option = input("\nSelect any option\n[i]nsert [d]elete [l]ist: ")

    if(chosen_option != "i" and chosen_option != "d" and chosen_option != "l"):
        print('Error: Invalid data. Try again and type just one letter')
        continue

    if(chosen_option == "i"):
        list_word = input("\nType any word: ")
        array_marlet_list.append(list_word)

    if(chosen_option == "d"):
        try:
             delete_word = input("\nType the index product: ")
             int_casting = int(delete_word)             
        except:
            print("Error: invalid input option. Try Again Just any index number character")    
            continue 

        if(int_casting >= len(array_marlet_list)):
             print("Error: invalid input option. Try Again") 
        else:
            array_marlet_list.pop(int_casting)
            print("Success: deletion successful") 
                   

    if(chosen_option == "l"):
        if len(array_marlet_list)>=1:
            print("Product List: \n")
            for index,value in enumerate(array_marlet_list):
                print(index,value)
        else:  
            print("List is empty")

