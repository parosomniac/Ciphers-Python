''' file to test all ciphers
 ensure that they can all handle uppercase, 
 lowercase, spaces, numbers, & special characters
'''

import ciphers

# Atbash 
def testAtbash():
    # a -> z
    assert ciphers.atbashEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`") == "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    # z -> a
    assert ciphers.atbashEncodeDecode("ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`") == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    

# Caesar
def testCaesar():
    # encode shift of 13
    assert ciphers.caesarEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !#'$%&()[]{}*+=-_,./|:;<>?@^~`", 1, 13) == "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890 !#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    # decode shift of 1
    assert ciphers.caesarEncodeDecode("BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890 !#'$%&()[]{}*+=-_,./|:;<>?@^~`", 2, 1) == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !#'$%&()[]{}*+=-_,./|:;<>?@^~`"


# Affine 
def testAffine():
    # encode slope 3 intercept 20
    assert ciphers.affineEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`", 1, (3, 20)) == "UXADGJMPSVYBEHKNQTWZCFILORuxadgjmpsvybehknqtwzcfilor1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    # decode slope 7 intercept 2
    assert ciphers.affineEncodeDecode("CJQXELSZGNUBIPWDKRYFMTAHOVcjqxelszgnubipwdkryfmtahov1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`", 2, (7, 2)) == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"

# Viginere
def testViginere():
    assert ciphers.viginereEncodeDecode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`", 1, "parosomniac") == "PBTRWTSUQJMAMECHEDFBUXLXPNspoqmfiwiaydazbxqthtljolkm1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"
    assert ciphers.viginereEncodeDecode("PBTRWTSUQJMAMECHEDFBUXLXPNspoqmfiwiaydazbxqthtljolkm1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`", 2, "parosomniac") == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !\"#'$%&()[]{}*+=-_,./|:;<>?@^~`"

