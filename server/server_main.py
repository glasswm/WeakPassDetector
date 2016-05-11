# -*- coding: utf-8 -*-

from famer import ask_db

__author__ = 'wm'

import logging
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        #self.cryptor = AES.new(self.key, self.mode, self.iv)

    def encrypt(self, text):
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        cryptor = AES.new(self.key, self.mode, self.iv)
        self.ciphertext = cryptor.encrypt(text)
        del cryptor
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        del cryptor
        return plain_text.rstrip('\0')

aes_obj = prpcrypt('wahaha5dezuiaiwo', '7418629350000312')

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs['foo'] + kwargs['bar']

@dispatcher.add_method
def check_weak_pass(**kwargs):
    support_encrypt_algorithm = ('md5', 'sha1')
    if ('encrypt_algorithm' not in kwargs or 'cipher_list' not in kwargs):
        logging.warning('invalid params')
        return 'invalid params'

    encrypt_algorithm = kwargs['encrypt_algorithm']
    cipher_list = kwargs['cipher_list']

    if encrypt_algorithm not in support_encrypt_algorithm:
        logging.warning('unsupport encrypt algorithm')
        return 'unsupport encrypt algorithm'
    elif cipher_list == None or len(cipher_list)==0:
        logging.warning('cipher list is empty')
        return 'cipher list is empty'
    else:
        cipher_list_low = []
        for i in cipher_list:
            cipher_list_low.append(i.lower())
        return ask_db(cipher_list_low, encrypt_algorithm)


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        aes_obj.decrypt(request.data), dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)