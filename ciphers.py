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
        res += letter_mapping[l]
    return res

def atbashDecode(message):
    pass

def caesarEncode(message):
    pass
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