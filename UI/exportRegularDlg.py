# -*- coding: utf-8 -*-
from time import sleep
import  wx
import wx.lib.masked as masked
from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType, generate_unmod_statement
from client.models import DBUtil

class exportRegularDialog(wx.Dialog):

    #cur_sys_info = None
    parent = None
    idx = None
    db_util = None

    def __init__(
            self, parent, ID, title, idx, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):

        self.parent = parent
        self.idx = idx
        self.db_util = DBUtil()
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        # This extra style can be set after the UI object has been created.
        if 'wxMac' in wx.PlatformInfo and useMetal:
            self.SetExtraStyle(wx.DIALOG_EX_METAL)


        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)

        box = wx.BoxSizer(wx.HORIZONTAL)
        self.m_Label_Day = wx.StaticText(self,wx.ID_ANY, u"限制天数",style = wx.ALIGN_CENTER)
        self.m_Text_Day = wx.TextCtrl(self)
        box.Add(self.m_Label_Day, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Text_Day, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
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
        rl = []
        count = 0
        if self.m_Text_Day.GetValue() == "":
            dlg = wx.MessageDialog(None, u"请输入限制天数!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            crypt_list = self.db_util.get_crypt_by_systemID(self.idx)
            for i in crypt_list:
                if i[2] >= int(self.m_Text_Day.GetValue()):
                    count += 1
                    temp = {'name' : 'aaaa1', 'day' : '31'}
                    temp['name'] = i[0]
                    temp['day'] = str(i[2])
                    rl.append(temp)
            print "input period: " + self.m_Text_Day.GetValue()
            generate_unmod_statement(self.parent.listBox.GetStringSelection(), u'汪明', rl, len(crypt_list), self.m_Text_Day.GetValue())

            print("export report")
            self.Destroy()

    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
#



