'''
Ciphers - Python
parosomniac
24 November 2024
A program that allows users to 
encode and decode messages using
some of the most common ciphers
'''

import ciphers

def switch_mode():
    user_input = -1
    while not (user_input == '1' or user_input == '2'):
        user_input = input("Would you like to encode(1) " + 
                           "or decode(2) a message?")
    return int(user_input)
        
def switch_menu(user_input):

    # Atbash cipher
    if user_input == 1:
        mode = switch_mode()
        # Atbash encode message
        if mode == 1:
            message = input("Enter a message to encode.")
            print(ciphers.atbashEncode(message))
        # Atbash decode message
        else:
            pass

    # Caesar cipher
    elif user_input == 2:
        pass
    # Affine cipher
    elif user_input == 3:
        pass

    # Viginere cipher
    elif user_input == 4:
        pass
    

def main():
    user_input = 0
    # print menu options
    while not (user_input == -1):
        # try to convert user input to int
        try: 
            user_input = int(input("Select from the cipher options below or enter -1 to quit.\n"
                            + "1) Atbash Cipher\n" + 
                            "2) Caesar cipher\n" +
                            "3) Affine cipher\n" + 
                            "4) Viginere cipher\n"
                            "-1) Quit\n"))
            
            # switch user_input
            switch_menu(user_input)
        # except catch if not an int
        except:
            print('Please enter an integer from the menu options given.')

    print("Program ended.")

main()
