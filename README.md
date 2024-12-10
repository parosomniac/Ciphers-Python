# Ciphers-Python

## Atbash Cipher
* A cipher that encodes a message using the reverse of the alphabet

* Atbash decode function isn't necessary, you can simply run the encoded message back through the encoder

## Caesar Cipher
* A cipher that encodes a message by replacing each letter with a shifted letter X units away

## Affine Cipher
* A substitution cipher where each letter is mapped to its numeric equivalent, encrypted using a mathematical function and then turned back into a letter


* E(x) = (ax + b) mod m
* m = 26, the length of the alphabet
* Verify that the value chosen for a is coprime to m 

* D(x) = a^-1 (x - b) mod m 
* a^ -1 = modular multiplicative inverse

## Viginere Cipher
* A cipher that encodes text using a Caesar cipher based on a key
* E(x) = (x + k) mod 26
* D(x) = (x - k) mod 26

## TODO
* refactor code
* Caesar, Affine, Viginere - combine functions of encode and decode
    * add mode as parameter
* write tests 
https://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start 

## FUTURE ADDITIONS
* graphical user interface
* refactor to reduce repetition of code