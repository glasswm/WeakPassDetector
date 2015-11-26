import threading
import time

from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType
from client.models import DBUtil

class regularThread(threading.Thread): #The timer class is derived from the class threading.Thread
    parent = None
    db_user_name = None
    db_pass_wd =None
    crypt_list = []

    def __init__(self, parent, idx):
        self.parent = parent
        super(regularThread, self).__init__()
        self._stop = threading.Event()

        db_util = DBUtil()
        self.crypt_list = db_util.get_crypt_by_systemID(idx)

    def run(self): #Overwrite run() method, put what you want the thread do here
        print("todo:regular test")
        # for i in self.crypt_list:


    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def set_db_user(self, name, passwd):
        self.db_user_name = name
        self.db_pass_wd = passwd