# -*- coding: utf-8 -*-

from famer import ask_db

__author__ = 'wm'

import logging
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

from cryptography.fernet import Fernet
key = 'M3ZkzmsiNCJHoV57K3dG0r4-gtkhfdpYMAlRoIZg4Kg='
encrypt_obj = Fernet(key)

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs['foo'] + kwargs['bar']

@dispatcher.add_method
def check_weak_pass(**kwargs):
    print "enter"
    support_encrypt_algorithm = ('md5', 'sha1', 'isc', 'oracle10', 'oracle11', 'sapg', 'sapb')
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
        print len(cipher_list)
        for i in cipher_list:
            cipher_list_low.append(i.lower())
        return ask_db(cipher_list_low, encrypt_algorithm)

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        encrypt_obj.decrypt(request.data), dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)