''' file to test all ciphers
 ensure that they can all handle uppercase, 
 lowercase, spaces, numbers, & special characters
'''

import ciphers

# Atbash 
def testAtbash():
    assert ciphers.atbashEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`") == "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    assert ciphers.atbashEncodeDecode('a') == 'z'
    
# Caesar
def testCaesar():
    # shift of 13
    assert ciphers.caesarEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`", 1, 13) == "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"

# Affine 
def testAffine():
    pass

# Viginere
def testViginere():
    pass

