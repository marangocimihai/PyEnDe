#!/usr/bin/python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto import Random
import base64

BLOCK_SIZE = 32
INTERRUPT = u'\u0001'
PAD = u'\u0000'
SECRET_KEY = "SecretRandomKey8"
IV = "SecretRandomIV93"

class Anonymize():
    @staticmethod
    def add_padding(data, interrupt, pad, block_size):
        new_data = ''.join([data, interrupt])
        new_data_len = len(new_data)
        remaining_len = block_size - new_data_len
        to_pad_len = remaining_len % block_size
        pad_string = pad * to_pad_len
        return ''.join([new_data,pad_string])

    @staticmethod
    def strip_padding(data, interrupt, pad):
        return data.rstrip(pad).rstrip(interrupt)

    @staticmethod
    def cipher_for_encryption():
        return AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    @staticmethod
    def cipher_for_decryption():
        return AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    @staticmethod
    def encrypt(plaintext_data):
        plaintext_padded = Anonymize.add_padding(plaintext_data, INTERRUPT, PAD, BLOCK_SIZE)
        encrypted = Anonymize.cipher_for_encryption().encrypt(plaintext_padded)
        return base64.b64encode(encrypted)

    @staticmethod
    def decrypt(encrypted_data):
        decoded_encrypted_data = base64.b64decode(encrypted_data)
        decrypted_data = Anonymize.cipher_for_decryption().decrypt(decoded_encrypted_data)
        return Anonymize.strip_padding(decrypted_data, INTERRUPT, PAD)

# our_data_to_encrypt = 'abc11100jgj56jku;u456$&*^(%NMJ:L"P    o78ri7000'
# encrypted_data = Anonymize.encrypt(our_data_to_encrypt)
# print 'Encrypted string:', encrypted_data
#
# decrypted_data = Anonymize.decrypt(encrypted_data)
# print 'Decrypted string:', decrypted_data