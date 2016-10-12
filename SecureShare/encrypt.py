__author__ = 'nc4sq'

import os.path
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def secret_string(input_message, enc_input_key):
    message = input_message.encode()
    public_key = enc_input_key.publickey()
    enc_data = public_key.encrypt(message, 32)
    return enc_data
    # print(enc_data)
    # print(enc_input_key.decrypt(enc_data))
    

def encrypt(message, enc_input_key, key_size=256):
    key = str(enc_input_key)
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, dec_input_key):
    key = str(dec_input_key)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(enc_input_filename, enc_file_input_key):
    try:
        file = open(enc_input_filename, 'rb')
    except IOError:
        print('There was an error opening the file!')
        return False
    newKey = str(enc_file_input_key)
    if len(str(enc_file_input_key)) < 16:
        string_val = 'abcdabcdabcdabcd'
        newKey = enc_file_input_key + string_val
    key16 = newKey[0:16]
    # key = str.encode(key16)
    key = key16
    with open(enc_input_filename, 'rb') as f:
        plaintext = f.read()
    enc = encrypt(plaintext, key)
    with open(enc_input_filename + ".enc", 'wb') as f:
        f.write(enc)
        return True
    return False

def decrypt_file(dec_input_filename, dec_file_input_key):
    if not os.path.isfile(dec_input_filename):
        print('There was an error opening the file!')
        return False
    else:
        newKey = str(dec_file_input_key)
        if len(str(dec_file_input_key)) < 16:
            string_val = 'abcdabcdabcdabcd'
            newKey = dec_file_input_key + string_val
        key16 = newKey[0:16]
        # key = str.encode(key16)
        key = key16
        with open(dec_input_filename, 'rb') as f:
            ciphertext = f.read()
        dec = decrypt(ciphertext, key)
        with open("DEC_" + dec_input_filename[:-4], 'wb') as f:
            f.write(dec)
            return True
        return False

# if __name__ == '__main__':
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

print("Testing secret_string\n")
print(secret_string('my name is deepak', key))

print("Testing encrypt_file\n")
print(encrypt_file('test.txt', key))

print("Testing decrypt_file\n")
print(decrypt_file('test.txt.enc', key))