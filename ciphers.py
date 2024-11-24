# file containing all of the ciphers

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
    pass

def affineEncode(message):
    pass
def affineDecode(message):
    pass

def viginereEncode(message):
    pass
def viginereDecode(message):
    pass