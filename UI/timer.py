# -*- coding: utf-8 -*-

import threading
import time
from datetime import datetime

from client.client_test import check_weakpass, add_log
from client.common import EncryptAlgorithmType
from client.models import DBUtil

class timer(threading.Thread): #The timer class is derived from the class threading.Thread
    cur_sys_info = None
    parent = None
    db_user_name = None
    db_pass_wd =None

    def __init__(self, parent, idx):
        self.parent = parent
        super(timer, self).__init__()
        self._stop = threading.Event()

        db_util = DBUtil()
        self.cur_sys_info = db_util.get_system_by_id(idx)

    def run(self): #Overwrite run() method, put what you want the thread do here
        #print 'db user: ', self.db_user_name, ', db_passwd: ', self.db_pass_wd
        self.parent.weak_List = []
        up_pair = self.cur_sys_info.get_account_data(username=self.db_user_name, password=self.db_pass_wd)
        begin_time = datetime.now()
        add_log(str(begin_time) + " - Start Check - " + repr(self.cur_sys_info) + " - Total Accounts " + str(len(up_pair)))
        username_list = []
        crypt_list = []
        for i in up_pair:
            username_list.append(i[0])
            crypt_list.append(i[1])
        self.parent.username_List = username_list
        #print username_list
        #print crypt_list

        if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            crypt_type = 'md5'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            crypt_type = 'sha1'

        while(self.stopped() != True):
            self.parent.m_ListCtrl.DeleteAllItems()
            weakCount = 0
            (weak_list, strong_list, unknown_count, weak_type_list) = check_weakpass(crypt_type, crypt_list)
            self.parent.weak_List = weak_list
            self.parent.m_Text_WeakNum.SetValue(str(len(weak_list)))
            self.parent.m_Text_SumNum.SetValue(str(len(up_pair)))
            self.parent.m_Text_UnknownNum.SetValue(str(unknown_count))

            for i in weak_list:
                self.parent.m_ListCtrl.InsertStringItem(weakCount,str(weakCount+1))
                self.parent.m_ListCtrl.SetStringItem(weakCount,1,username_list[i])
                self.parent.m_ListCtrl.SetStringItem(weakCount,2,weak_type_list[weakCount])
                weakCount += 1
            self.parent.m_Gauge.SetValue(100-unknown_count*100/len(up_pair))
            if unknown_count == 0:
                add_log(str(datetime.now()) + " - End Check " + str(begin_time) + " - " + repr(self.cur_sys_info) + " - Weak Accounts " + str(len(weak_list)))
                break
            time.sleep(20)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def set_db_user(self, name, passwd):
        self.db_user_name = name
        self.db_pass_wd = passwd