# file containing all of the ciphers

letters_nums_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                        'f': 5, 'g':6, 'h':7, 'i':8, 'j':9,
                        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
                        'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                        'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def atbashEncode(message):
    res = ''
    letter_mapping = {'a': 'z', 'b': 'y', 'c':'x', 'd':'w',
                      'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 
                      'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 
                      'm': 'n', 'n': 'm', 'o':'l', 'p': 'k', 
                      'q': 'j', 'r': 'i', 's':'h', 't': 'g', 
                      'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 
                      'y': 'b', 'z': 'a'}
    
    for l in message:
        if l.isalpha():
            if l.islower():
                res += letter_mapping[l]
            else:
                # if the letter is capitalized, match uncapitalized then capitalize
                res += letter_mapping[l.lower()].upper()
        else:
            res += l
    return res

def caesarEncode(message):
    shift = 0
    while not (shift > 0):
        try:
            shift = int(input("How much is the shift for the cipher? "))
            shift %= 26
            encryptedMsg = ''
            for c in message:
                if c.isalpha() and c.islower():
                    ascii_num = ord(c)
                    ascii_num += shift
                    if (ascii_num > 122):
                        ascii_num = ascii_num % 122 + 97 - 1
                    c = chr(ascii_num)
                    encryptedMsg += c
                elif c.isalpha() and c.isupper():
                    ascii_num = ord(c)
                    ascii_num += shift
                    if (ascii_num > 90):
                        ascii_num = ascii_num % 90 + 65 - 1
                    c = chr(ascii_num)
                    encryptedMsg += c
                else:
                    encryptedMsg += c
            return encryptedMsg
        except:
            print("Shift must be an integer greater than 0.")

def caesarDecode(message):
    shift = 0
    while not (shift > 0):
        try:
            shift = int(input("How much is the shift for the cipher? "))
            shift %= 26
            decryptedMsg = ''
            for c in message:
                if c.isalpha() and c.islower():
                    ascii_num = ord(c)
                    ascii_num -= shift
                    if (ascii_num < 97):
                        ascii_num = 122 - 97 % ascii_num + 1
                    c = chr(ascii_num)
                    decryptedMsg += c
                elif c.isalpha() and c.isupper():
                    ascii_num = ord(c)
                    ascii_num -= shift
                    if (ascii_num < 65):
                        ascii_num = 90 - 65 % ascii_num + 1
                    c = chr(ascii_num)
                    decryptedMsg += c
                else:
                    decryptedMsg += c
            return decryptedMsg
        except:
            print("Shift must be an integer greater than 0.")

# no common factors other than 1
def isCoprime(num):
    factors_26 = set([2, 13, 26]) # 1 is a factor of every number, so removed
    factors = set([num]) # the number itself is always a factor
    # coprime numbers have a highest common factor of 1
    # divide num by whole numbers starting with 1
    # if it results in a whole number with no remainder, then divisor and quotient are factors of the original num
    # break when quotient is smaller than divisor
    d = 2
    q = float("inf")
    while q > d:
        q = num / d
        if num % d == 0:
            factors.add(int(q))
            factors.add(d)
        d += 1
    # return there are no matches
    return not set.intersection(factors_26, factors)

def affineEncode(message):
    # E(x) = (ax +b) mod m
    m = 26 # size of the alphabet

    # a = slope, must be coprime to the size of the alphabet
    # b = intercept
    a = -1
    b = -1
    while not (a >= 1):
        try:

            a = int(input("a: Input a positive integer that is coprime to 26. "))
            while not(isCoprime(a)):
                a = int(input("'a' must be coprime to 26."))

            while not(b >= 1):
                try:
                    b = int(input("b: Input an intercept value to help encode the message. "))
                    encryptedMsg = ""
                    upper_c = False
                    for c in message:
                        if c.isalpha():
                            # if letter was uppercase
                            if c.isupper():
                                upper_c = True
                                c = c.lower()
                            num = letters_nums_mapping[c]
                            num = (a * num + b) % m 
                            # get new encrypted character by looking up the letter associated with the new number
                            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
                            if upper_c == True:
                                encryptedMsg += c.upper()
                                upper_c = False
                            else:
                                encryptedMsg += c
                            
                except:
                    print("The number must be a positive integer. ")
                    b = -1
        except:
            print("The number must not have any common factors with 26 other than 1. ")
            a = -1
    return encryptedMsg

def getModInverse(a, mod):
    for i in range(1, mod):
        if (((a % mod) * (i % mod)) % mod == 1):
            return i

def affineDecode(message):
    # retrieve a and b from user
    m = 26 # size of the alphabet

    # a = slope, must be coprime to the size of the alphabet
    # b = intercept
    a = -1
    b = -1
    while not (a >= 1):
        try:

            a = int(input("a: Input the positive integer coprime to 26 used to encode the message. "))
            while not(isCoprime(a)):
                a = int(input("'a' must be coprime to 26."))

            while not(b >= 1):
                try:
                    b = int(input("b: Input the intercept value used to encode the message. "))
                    decryptedMsg = ""
                    upper_c = False
                    for c in message:
                        if c.isalpha():
                            # if letter was uppercase
                            if c.isupper():
                                upper_c = True
                                c = c.lower()
                            # convert char to num
                            num = letters_nums_mapping[c]
                            # TODO: fix this section
                            num = getModInverse(a, m) * (num - b) % m
                            print(num)
                            # get new encrypted character by looking up the letter associated with the new number
                            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
                            if upper_c == True:
                                decryptedMsgdMsg += c.upper()
                                upper_c = False
                            else:
                                decryptedMsg += c
                            
                except:
                    print("The number must be a positive integer. ")
                    b = -1
        except:
            print("The number must not have any common factors with 26 other than 1. ")
            a = -1
    return decryptedMsg


def viginereEncode(message):
    pass
def viginereDecode(message):
    pass


print(affineDecode('DkMM'))