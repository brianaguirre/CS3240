__author__ = 'BrianAguirre'

"""
For this homework I used the following resources:
Resources:
How Encryption and Decryption Work
http://www.encryptionanddecryption.com/encryption/
Python and cryptography with pycrypto
http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
Python Cryptography Toolkit
https://www.dlitz.net/software/pycrypto/

They were provided by the instructor Professor Tom Horton. Fall 2015

"""

import os
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3
from Crypto.Cipher import ARC4


enc = None
dec = None
encrypted_txt = None
key_val = None

def encrypt_file(in_file, key):
    global enc
    enc = ARC4.new(key)
    global dec
    dec = ARC4.new(key)
    global encrypted_txt
    global key_val
    key_val = key

    out_file = in_file +".enc"
    with open(in_file, 'r') as in_file:
        with open(out_file, 'w') as out_file:
            while True:
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                else:
                    encrypted_txt = enc.encrypt(chunk)
                    out_file.write(str(encrypted_txt))
                    return True



def decrypt_file(in_file, key):
    file_name = in_file[:len(in_file)-4]
    out_file = "DEC_" + file_name
    global enc
    global dec
    global encrypted_txt

    if (key_val == key ):
        with open(in_file, 'r') as in_file:
            with open(out_file, 'w') as out_file:
                while True:
                    chunk = in_file.read()
                    if len(chunk) == 0:
                        break
                        return False
                    else:
                        out_file.write(str(dec.decrypt(encrypted_txt).decode('utf-8')))
                        return True
    else:
        print("Keys did not match. File could not be decoded.")
        return False



def secret_string(strng, key):
    #COMMENTED CODE: Tests encryption:
    obj1 = ARC4.new(key)
    #obj2 = ARC4.new(key)
    secret = obj1.encrypt(strng)

    #print (strng)
    #print (key)
    #print (obj2.decrypt(secret))
    return secret