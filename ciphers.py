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
                # letter is capitalized, match lower then capitalize
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
                if c.isalpha():
                    ascii_num = ord(c)
                    ascii_num += shift
                    if c.islower():
                        if (ascii_num > 122):
                            ascii_num = ascii_num % 122 + 97 - 1
                    else:
                        if (ascii_num > 90):
                            ascii_num = ascii_num % 90 + 65 -1
                    c = chr(ascii_num)
                    encryptedMsg += c 
                else:
                    encryptedMsg += c
            return encryptedMsg
        except:
            print("Shift must be an integer greater than 0. ")


def caesarDecode(message):
    shift = 0
    while not (shift > 0):
        try:
            shift = int(input("How much is the shift for the cipher? "))
            shift %= 26
            decryptedMsg = ''
            for c in message:
                if c.isalpha():
                    ascii_num = ord(c)
                    ascii_num -= shift
                    if c.islower():
                        if (ascii_num < 97):
                            ascii_num = 122 - 97 % ascii_num + 1
                    else:
                        if (ascii_num < 65):
                            ascii_num = 90 - 65 % ascii_num + 1
                    c = chr(ascii_num)
                    decryptedMsg += c 
                else:
                    decryptedMsg += c
            return decryptedMsg
        except:
            print("Shift must be an integer greater than 0. ")


# no common factors other than 1
def isCoprime(num):
    factors_26 = set([2, 13, 26])
    factors = set([num])
    d = 2
    q = float("inf")
    while q > d:
        q = num / d
        if num % d == 0:
            factors.add(int(q))
            factors.add(d)
        d += 1
    return not set.intersection(factors, factors_26)


def affineEncode(message):
    # E(x) = (ax + b) mod m
    m = 26 # size of the alphabet
    a = - 1 # coprime to the alphabet
    b = -1 # intercept

    while not (a >= 1):
        try:
            a = int(input("a: Input a positive integer that is coprime to 26. "))
            while not(isCoprime(a)):
                a = int(input("'a' must be coprime to 26. "))
            while not(b >= 1):
                try:
                    b = int(input("b: Input an intercept value to help encode the message. "))
                    encryptedMsg = ""
                    upper_c = False
                    for c in message:
                        if c.isalpha():
                            if c.isupper():
                                upper_c = True
                                c = c.lower()
                            num = letters_nums_mapping[c]
                            num = (a * num + b) % m
                            # get new encrypted char by looking up letter of new num
                            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
                            if upper_c == True:
                                encryptedMsg += c.upper()
                                upper_c = False
                            else:
                                encryptedMsg += c
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
    m = 26
    a = -1
    b = -1
    while not (a >= 1):
        try:
            a = int(input("a: Input the positive integer coprime to 26 used to encode the message. "))
            while not(isCoprime(a)):
                a = int(input("'a' must be coprime to 26. "))
            while not(b >= 1):
                try:
                    b = int(input("b: Input the intercept value used to encode the message. "))
                    decryptedMsg = ""
                    upper_c = False
                    for c in message:
                        if c.isalpha():
                            if c.isupper():
                                upper_c = True
                                c = c.lower()
                            num = letters_nums_mapping[c]
                            num = getModInverse(a, m) * (num - b) % m
                            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
                            if upper_c == True:
                                decryptedMsg += c.upper()
                                upper_c = False
                            else:
                                decryptedMsg += c
                        else:
                            decryptedMsg += c
                except:
                    print("The number must be a positive integer ")
                    b = -1 
        except: 
            print("The number must not have any common factors with 26 other than 1. ")
            a = -1
    return decryptedMsg


def getKey():
    key = ""
    while not key or not key.isalpha():
        try:
            key = input("Input a key for the message. ")
        except:
            print("The key must be a string. ")
    return key


def viginereEncode(message):
    key = getKey()

    encryptedMsg = ""
    num = -1
    c_ptr = 0
    m = 26
    upper_c = False

    for c in message:
        if c.isalpha():
            if c.isupper():
                upper_c = True
                c = c.lower()
            # loop through indices of the key
            num = (letters_nums_mapping.get(c) + letters_nums_mapping.get(key[c_ptr])) % m 
            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
            c_ptr += 1
            # if ptr now greater than indices of key, reset
            if c_ptr > len(key) - 1:
                c_ptr = 0
            if upper_c == True:
                encryptedMsg += c.upper()
                upper_c = False
            else:
                encryptedMsg += c
        else:
            encryptedMsg += c
    return encryptedMsg


def viginereDecode(message):
    key = getKey()

    decryptedMsg = ""
    num = -1
    c_ptr = 0
    m = 26
    upper_c = False

    for c in message:
        if c.isalpha():
            if c.isupper():
                upper_c = True
                c = c.lower()
            num = (letters_nums_mapping.get(c) - letters_nums_mapping.get(key[c_ptr])) % m
            num = (num + m) % m
            c = (list(letters_nums_mapping.keys())[list(letters_nums_mapping.values()).index(num)])
            c_ptr += 1
            if c_ptr > len(key) - 1:
                c_ptr = 0
            if upper_c == True:
                decryptedMsg += c.upper()
                upper_c = False
            else:
                decryptedMsg += c
        else:
            decryptedMsg += c
    return decryptedMsg
