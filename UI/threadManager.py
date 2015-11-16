#-*- encoding:UTF-8 -*-
from time import sleep

import wx
import threading

from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType
from client.models import DBUtil


class WorkerThread(threading.Thread):
    cur_sys_info = None
    def __init__(self, threadNum, idx, parent, window):
        threading.Thread.__init__(self)
        self.threadNum = threadNum
        self.count = 0
        self.idx = idx
        self.parent = parent
        self.window = window
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear()

    def stop(self):
        self.timeToQuit.set()

    def run(self):
        db_util = DBUtil()
        self.cur_sys_info = db_util.get_system_by_id(self.idx)
        up_pair = self.cur_sys_info.get_account_data(username=self.m_Text_Name.GetValue(), password=self.m_Text_PSW.GetValue())
        username_list = []
        crypt_list = []
        for i in up_pair:
            username_list.append(i[0])
            crypt_list.append(i[1])
        print username_list
        print crypt_list
        weakCount = 0
        if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            crypt_type = 'md5'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            crypt_type = 'sha1'

        self.Destroy()
        self.parent.m_ListCtrl.DeleteAllItems()
        while(True):
            (weak_list, strong_list, unknown_count) = check_weakpass(crypt_type, crypt_list)
            self.parent.m_Text_WeakNum.SetValue(str(len(weak_list)))
            self.parent.m_Text_SumNum.SetValue(str(len(up_pair)))
            self.parent.m_Text_UnknownNum.SetValue(str(unknown_count))
            for i in weak_list:
                self.parent.m_ListCtrl.InsertStringItem(weakCount,str(weakCount+1))
                self.parent.m_ListCtrl.SetStringItem(weakCount,1,username_list[i])
                weakCount += 1
            self.parent.m_Gauge.SetValue(100-unknown_count*100/len(up_pair))
            if unknown_count == 0:
                break
            sleep(5)
