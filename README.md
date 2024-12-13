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


## Testing
* pip install pytest
* run in terminal with:

```python
C:\Users\paro2\AppData\Roaming\Python\Python313\Scripts\pytest.exe test_ciphers.py
```

## TODO 
* currently pytest not installed in virtual environment - fix

## FUTURE ADDITIONS
* (GUI) graphical user interface
