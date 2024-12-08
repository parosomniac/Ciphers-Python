

letters_nums_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                        'f': 5, 'g':6, 'h':7, 'i':8, 'j':9,
                        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
                        'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                        'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def getModInverse(a, mod):
    for i in range(1, mod):
        if (((a % mod) * (i % mod)) % mod == 1):
            return i

a = 3
b = 20
m = 26

upper_c = False
message = 'dkm'
decryptedMsg = ""

for c in message:
    if c.isalpha():
        # if letter was uppercase
        if c.isupper():
            upper_c = True
            c = c.lower()
        # convert char to num
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
print(decryptedMsg)