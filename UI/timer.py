# -*- coding: utf-8 -*-

import threading
import time
from datetime import datetime

from client.client_test import check_weakpass, add_log
from client.common import EncryptAlgorithmType
from client.models import DBUtil
from client.common import DatabaseType
import wx

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_list_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_list_hig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
char_set = num_list + letter_list_low + letter_list_hig

def string_all_in_set(test_str, test_set):
    for s in test_str:
        if s in test_set:
            pass
        else:
            return False
    return True

def is_md5_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 32:
        return False
    return True

def is_sha1_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 40:
        return False
    return True

def is_isc_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 56:
        return False
    return True

def is_oracle10_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 16:
        return False
    return True

def is_oracle11_crypt(crypt):
    if crypt == None:
        return False
    if len(crypt) <= 2:
        return False
    else:
        crypt = crypt[2:] #remove "S:"
    if not string_all_in_set(crypt, char_set) or len(crypt) != 60:
        return False
    return True

def is_sapg_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 40:
        return False
    return True

def is_sapb_crypt(crypt):
    if crypt == None:
        return False
    if not string_all_in_set(crypt, char_set) or len(crypt) != 16:
        return False
    return True


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
        if self.cur_sys_info.db_type is DatabaseType.file:
            up_pair = self.cur_sys_info.get_csv_data(self.cur_sys_info.db_name)
        else:
            up_pair = self.cur_sys_info.get_account_data(username=self.db_user_name, password=self.db_pass_wd)
        if len(up_pair) < 1:
            dlg = wx.MessageDialog(None, u"没有获取到待破解数据", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            return
        if len(up_pair) > 1000:
            dlg = wx.MessageDialog(None, u"试用版最多仅支持1000条口令!", u"提示", wx.OK | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
        print 'First 3 records:'
        for i in up_pair[0:3]:
            print 'username: ' + i[0] + ', password_encrypt: ' + i[1]
        begin_time = datetime.now()
        try:
            add_log(str(begin_time) + " - Start Check - " + repr(self.cur_sys_info) + " - Total Accounts " + str(len(up_pair)))
        except:
            pass
        username_list = []
        crypt_list = []
        invalid_crypt_count = 0
        if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            for i in up_pair:
                if is_md5_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append(i[1])
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            for i in up_pair:
                if is_sha1_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append(i[1])
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.isc:
            for i in up_pair:
                if is_isc_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append(i[1])
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle10:
            for i in up_pair:
                if is_oracle10_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append("%s:%s" % (i[1],i[0]))
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle11:
            for i in up_pair:
                if is_oracle11_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append("%s:%s" % (i[1][2:42],i[1][-20:]))
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapg:
            for i in up_pair:
                if is_sapg_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append("%s$%s" % (i[0],i[1]))
                else:
                    invalid_crypt_count += 1
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapb:
            for i in up_pair:
                if is_sapb_crypt(i[1]):
                    username_list.append(i[0])
                    crypt_list.append("%s$%s" % (i[0],i[1]))
                else:
                    invalid_crypt_count += 1
        print '%d invalid crypts found' % invalid_crypt_count

        if float(invalid_crypt_count) / float(len(up_pair)) > 1.0/3.0:
            dlg = wx.MessageDialog(None, u"加密算法类别设置不正确，请与被测系统管理员进行核实", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            return
        self.parent.username_List = username_list
        #print username_list
        #print crypt_list

        if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            crypt_type = 'md5'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            crypt_type = 'sha1'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.isc:
            crypt_type = 'isc'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle10:
            crypt_type = 'oracle 7-10'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle11:
            crypt_type = 'oracle11'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapg:
            crypt_type = 'sapg'
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapb:
            crypt_type = 'sapb'

        while(self.stopped() != True):
            self.parent.m_ListCtrl.DeleteAllItems()
            weakCount = 0
            (weak_list, strong_list, unknown_count, weak_type_list) = check_weakpass(crypt_type, crypt_list)
            self.parent.weak_List = weak_list
            self.parent.weak_type_list = weak_type_list
            self.parent.m_Text_WeakNum.SetValue(str(len(weak_list)))
            self.parent.m_Text_SumNum.SetValue(str(len(crypt_list)))
            self.parent.m_Text_UnknownNum.SetValue(str(unknown_count))

            for i in weak_list:
                self.parent.m_ListCtrl.InsertStringItem(weakCount,str(weakCount+1))
                self.parent.m_ListCtrl.SetStringItem(weakCount,1,username_list[i])
                self.parent.m_ListCtrl.SetStringItem(weakCount,2,weak_type_list[weakCount])
                weakCount += 1
            self.parent.m_Gauge.SetValue(100-unknown_count*100/len(crypt_list))
            if len(weak_list) + len(strong_list) == len(crypt_list):
                dlg = wx.MessageDialog(None, u"检测完成，请导出报表查看详情", u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                try:
                    add_log(str(datetime.now()) + " - End Check " + str(begin_time) + " - " + repr(self.cur_sys_info) + " - Weak Accounts " + str(len(weak_list)))
                except:
                    pass
                break
            time.sleep(40)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def set_db_user(self, name, passwd):
        self.db_user_name = name
        self.db_pass_wd = passwd