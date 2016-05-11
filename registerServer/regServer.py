from models import DBUtil
from datetime import datetime
from models import UseLog

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

logging.basicConfig(filename='use.log', level=logging.INFO)

@dispatcher.add_method
def verify(**kwargs):
    if ('serial_key' not in kwargs):
        logging.warning('invalid params: serial_key not exist')
        return -2

    serial_key = kwargs['serial_key']
    db_util = DBUtil()
    res = db_util.check_serial(serial_key)
    del db_util
    return res

@dispatcher.add_method
def addLog(**kwargs):
    if ('message' not in kwargs):
        logging.warning('invalid params: message not exist')
        return -1
    message =  kwargs['message']
    db_util = DBUtil()
    db_util.add_use_log(UseLog(message=message, log_time=datetime.now()))
    del db_util
    return 0

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    logging.error(str(datetime.now()) + ' - ' + request.remote_addr + ' - ' + aes_obj.decrypt(request.data))
    response = JSONRPCResponseManager.handle(
        aes_obj.decrypt(request.data), dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4001, application)