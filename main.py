'''
Ciphers - Python
parosomniac
24 November 2024
A program that allows users to 
encode and decode messages using
4 of the most common ciphers
'''

import ciphers

def switch_mode():
    user_input = -1
    while not(user_input == '1' or user_input == '2'):
        user_input = input("Would you like to encode(1) " + 
                           "or decode(2) a message? ")
    return int(user_input)


def switch_menu(user_input):
    if user_input == -1:
        return
    
    mode = switch_mode()
    message = input("Enter your message: ")

    # Atbash cipher
    if user_input == 1:
        print(ciphers.atbashEncodeDecode(message))

    # Caesar cipher
    elif user_input == 2:
        print(ciphers.caesarEncodeDecode(message, mode))
        
    # Affine cipher
    elif user_input == 3:
        print(ciphers.affineEncodeDecode(message, mode))

    # Viginere cipher
    elif user_input == 4:
       
        print(ciphers.viginereEncodeDecode(message, mode))
    

def main():
    user_input = 0

    while not (user_input) == -1:
        try:
            user_input = int(input("\nSelect from the cipher options below or enter -1 to quit.\n"
                            + "1) Atbash Cipher\n" + 
                            "2) Caesar cipher\n" +
                            "3) Affine cipher\n" + 
                            "4) Viginere cipher\n"
                            "-1) Quit\n"))
            
            switch_menu(user_input)

        except:
            print('Please enter an integer from the menu options given. ')

    print("Program ended.")

main()