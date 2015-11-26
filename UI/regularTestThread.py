import threading
import time

from interface import crypt, updateDtime
from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType
from client.models import DBUtil
import datetime

class regularThread(threading.Thread): #The timer class is derived from the class threading.Thread
    parent = None
    db_user_name = None
    db_pass_wd = None
    db_util = None
    idx = None
    #crypt_list = []

    def __init__(self, parent, idx):
        self.parent = parent
        super(regularThread, self).__init__()
        self._stop = threading.Event()

        self.db_util = DBUtil()
        self.idx = idx
        # self.cur_sys_info = db_util.get_system_by_id(idx)
        # self.crypt_list = db_util.get_crypt_by_systemID(idx)

    def run(self): #Overwrite run() method, put what you want the thread do here
        print("todo:regular test")
        cur_sys_info = self.db_util.get_system_by_id(self.idx)
        up_pair = self.cur_sys_info.get_account_data(username=self.db_user_name, password=self.db_pass_wd)
        up_pair_crypt = []
        for i in up_pair:
            temp = (i[0],crypt(i[1]))
            up_pair_crypt.append(temp)

        #if table not exists, set up_pair_crypt to db

        crypt_list = self.db_util.get_crypt_by_systemID(self.idx)
        new_list = []
        symbol = False
        #dTime = updateDtime('2015-11-05')
        now = datetime.datetime.now()
        dTime = (now - cur_sys_info.last_update_time).days
        cur_sys_info.last_update_time = now
        self.db_util.update_system(cur_sys_info)

        for i in up_pair_crypt:
            for j in crypt_list:
                if i[0] != j[0]:
                    symbol = True
                    continue
                else:
                    symbol = False
                    if i[1] != j[1]:
                        temp = (i[0],i[1],0)
                    else:
                        temp = (i[0],i[1],j[2] + dTime)
            if symbol == True:
                temp = (i[0],i[1],0)
                symbol = False
            new_list.append(temp)

        self.db_util.set_crypt(self.idx, new_list)
        self.parent.m_Gauge.SetValue(100)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def set_db_user(self, name, passwd):
        self.db_user_name = name
        self.db_pass_wd = passwd