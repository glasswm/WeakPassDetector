# -*- coding: utf-8 -*-
from time import sleep
import  wx
import time
import datetime
import wx.lib.masked as masked

from client.__setting__ import detect_period
from interface import crypt
from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType
from client.models import DBUtil

class ReguTestDialog(wx.Dialog):

    parent = None
    db_util = None
    idx = None

    def __init__(
            self, parent, ID, title, idx, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):
        self.db_util = DBUtil()
        self.idx = idx
        self.parent = parent
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        if 'wxMac' in wx.PlatformInfo and useMetal:
            self.SetExtraStyle(wx.DIALOG_EX_METAL)

        sizer = wx.BoxSizer(wx.VERTICAL)

        box = wx.BoxSizer(wx.HORIZONTAL)
        self.m_Label_Name = wx.StaticText(self,wx.ID_ANY, u"用户名",style = wx.ALIGN_CENTER)
        self.m_Text_Name = wx.TextCtrl(self)
        box.Add(self.m_Label_Name, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Text_Name, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_PSW = wx.StaticText(self, wx.ID_ANY, u"密码",style = wx.ALIGN_CENTER)
        self.m_Text_PSW = wx.TextCtrl(self, style=wx.TE_PASSWORD)

        box.Add(m_Label_PSW, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Text_PSW, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        bt_Ok = wx.Button(self,wx.ID_ANY,label=u"确定")
        bt_Cancel = wx.Button(self,wx.ID_ANY,label=u"取消")
        box.Add(bt_Ok,1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(bt_Cancel,1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

        self.Bind(wx.EVT_BUTTON, self.OK_button, bt_Ok)
        self.Bind(wx.EVT_BUTTON, self.Cancel_Button, bt_Cancel)

    def OK_button(self, evt):
        #print("ok!")
        if self.m_Text_Name == "" or self.m_Text_PSW == "":
            dlg = wx.MessageDialog(None, u"请输入完整信息!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            print("regular modify testing!")
            self.regularTest()
            self.Destroy()

    def regularTest(self):
        cur_sys_info = self.db_util.get_system_by_id(self.idx)
        up_pair = cur_sys_info.get_account_data(username=self.m_Text_Name.GetValue(), password=self.m_Text_PSW.GetValue())
        up_pair_crypt = []
        for i in up_pair:
            temp = (i[0],crypt(i[1]))
            up_pair_crypt.append(temp)

        #if table not exists, set up_pair_crypt to db

        crypt_list = self.db_util.get_crypt_by_systemID(self.idx)
        d = {}
        for i in crypt_list:
            d[i[0]] = (i[1],i[2])

        new_list = []

        now = datetime.datetime.now()
        if cur_sys_info.last_update_time == None:
            dTime = 0
        else:
            dTime = (now - cur_sys_info.last_update_time).days
        cur_sys_info.last_update_time = now
        self.db_util.update_system(cur_sys_info)

        count = 0
        for i in up_pair_crypt:
            temp1 = None
            if d.has_key(i[0]) == True:
                if i[1] == d[i[0]][0]:
                    temp1 = (i[0],i[1],d[i[0]][1] + dTime)
                    if temp1[2] >= detect_period:
                        self.parent.m_ListCtrl.InsertStringItem(count,str(count+1))
                        self.parent.m_ListCtrl.SetStringItem(count,1,temp1[0])
                        self.parent.m_ListCtrl.SetStringItem(count,2,str(temp1[2]))
                        count += 1
                else:
                    temp1 = (i[0],i[1],0)
            else:
                temp1 = (i[0],i[1],0)
            new_list.append(temp1)

        self.db_util.set_crypt(self.idx, new_list)
        self.parent.m_Gauge.SetValue(100)

    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
#



