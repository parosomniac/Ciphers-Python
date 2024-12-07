
letters_nums_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                        'f': 5, 'g':6, 'h':7, 'i':8, 'j':9,
                        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
                        'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                        'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


def getModInverse(a, mod):
    for i in range(1, mod):
        if (((a % mod) * (i % mod)) % mod == 1):
            return i

num = 3 
m = 26
a = 3
b = 20

word = "DkMM" # -> DoGG 3 14 6 6 
for c in word:
    if c.isupper():
        upper_c = True
        c = c.lower()
    # convert char to num
    num = letters_nums_mapping[c]
    num = getModInverse(a, m) * (num - b) % m
    print(num)
    if upper_c == True:
        upper_c = False