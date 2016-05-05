from models import DBUtil
from datetime import datetime
from models import UseLog

__author__ = 'wm'

import logging
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher


logging.basicConfig(filename='use.log', level=logging.INFO)

@dispatcher.add_method
def verify(**kwargs):
    if ('serial_key' not in kwargs):
        logging.warning('invalid params: serial_key not exist')
        return -2

    serial_key = kwargs['serial_key']
    db_util = DBUtil()
    return db_util.check_serial(serial_key)

@dispatcher.add_method
def addLog(**kwargs):
    if ('message' not in kwargs):
        logging.warning('invalid params: message not exist')
        return -1
    message =  kwargs['message']
    db_util = DBUtil()
    db_util.add_use_log(UseLog(message=message, log_time=datetime.now()))
    return 0

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    logging.info(str(datetime.now()) + ' - ' + request.remote_addr + ' - ' + request.data)
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4001, application)