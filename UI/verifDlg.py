# -*- coding: utf-8 -*-
from time import sleep
import  wx
import wx.lib.masked as masked
from client.client_test import check_weakpass
from client.common import EncryptAlgorithmType
from client.models import DBUtil


class VerifDialog(wx.Dialog):

    cur_sys_info = None
    parent = None

    def __init__(
            self, parent, ID, title, idx, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):
        self.parent = parent
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
        self.m_Label_Name = wx.StaticText(self,wx.ID_ANY, u"用户名",style = wx.ALIGN_CENTER)
        self.m_Text_Name = wx.TextCtrl(self)
        box.Add(self.m_Label_Name, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Text_Name, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
  
        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_PSW = wx.StaticText(self, wx.ID_ANY, u"密码",style = wx.ALIGN_CENTER)
        self.m_Text_PSW = wx.TextCtrl(self)

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

        db_util = DBUtil()
        self.cur_sys_info = db_util.get_system_by_id(idx)
        
    def OK_button(self, evt):
        print("ok!")
        if self.m_Text_Name == "" or self.m_Text_PSW == "":
            dlg = wx.MessageDialog(None, u"请输入完整信息!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            self.parent.thread.start()
            # up_pair = self.cur_sys_info.get_account_data(username=self.m_Text_Name.GetValue(), password=self.m_Text_PSW.GetValue())
            # username_list = []
            # crypt_list = []
            # for i in up_pair:
            #     username_list.append(i[0])
            #     crypt_list.appendi[1])
            # print username_list
            # print crypt_list
            # weakCount = 0
            # if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            #     crypt_type = 'md5'
            # elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            #     crypt_type = 'sha1'
            #
            # self.Destroy()
            # self.parent.m_ListCtrl.DeleteAllItems()
            # while(True):
            #     (weak_list, strong_list, unknown_count) = check_weakpass(crypt_type, crypt_list)
            #     self.parent.m_Text_WeakNum.SetValue(str(len(weak_list)))
            #     self.parent.m_Text_SumNum.SetValue(str(len(up_pair)))
            #     self.parent.m_Text_UnknownNum.SetValue(str(unknown_count))
            #     # self.parent.m_Text_WeakNum.update()
            #     # self.parent.m_Text_SumNum.update()
            #     # self.parent.m_Text_UnknownNum.update()
            #     #self.parent.count = 100-unknown_count*100/len(up_pair)
            #     for i in weak_list:
            #         #print weakCount+i
            #         self.parent.m_ListCtrl.InsertStringItem(weakCount,str(weakCount+1))
            #         self.parent.m_ListCtrl.SetStringItem(weakCount,1,username_list[i])
            #         weakCount += 1
            #     self.parent.m_Gauge.SetValue(100-unknown_count*100/len(up_pair))
            #     if unknown_count == 0:
            #         break
            #     sleep(5)


        # m_ListCtrl.SetStringItem(0,1,u"信息系统")

    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
#             


 
