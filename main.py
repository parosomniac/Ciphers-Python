'''
Ciphers - Python
parosomniac
24 November 2024
A program that allows users to 
encode and decode messages using
some of the most common ciphers
'''
import ciphers

def switch(input):

    # Atbash cipher
    if input == 1:

    # Caesar cipher
    elif input == 2:
    # Affine cipher
    elif input == 3:

    # Viginere cipher
    elif input == 4:
    

def main():
    user_input = 0
    # print menu options
    while user_input != -1:
        user_input = input("Select from the cipher options below or enter -1 to quit.\n"
                        + "1) Atbash Cipher\n" + 
                        "2) Caesar cipher\n" +
                        "3) Affine cipher\n" + 
                        "4) Viginere cipher\n"
                        "-1) Quit\n")
        # switch user_input
        switch(user_input)

    print("Program ended.")
main()
