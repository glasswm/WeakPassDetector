import os
from models import DBUtil
from datetime import datetime
from models import UseLog

__author__ = 'wm'

import logging
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

from cryptography.fernet import Fernet
key = 'M3ZkzmsiNCJHoV57K3dG0r4-gtkhfdpYMAlRoIZg4Kg='
encrypt_obj = Fernet(key)

logging.basicConfig(filename=os.path.dirname(__file__) + '/use.log', level=logging.INFO)

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

    logging.error(str(datetime.now()) + ' - ' + request.remote_addr + ' - ' + encrypt_obj.decrypt(request.data))
    response = JSONRPCResponseManager.handle(
        encrypt_obj.decrypt(request.data), dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4001, application)