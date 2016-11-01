# -*- coding: utf-8 -*-
import  wx
import wx.lib.masked as masked
from client.common import EncryptAlgorithmType, DatabaseType, crypt_type_list, db_type_list
from client.models import DBUtil, SystemInfo
import os

class EditSysDialog2(wx.Dialog):

    cur_sys_info = None

    def __init__(
            self, parent, ID, title, info, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False
            ):

        self.cur_sys_info = info
        # Instead of calling wx.Dialog.__init__ we precreate the dialog
        # so we can set an extra style that must be set before
        # creation, and then we create the GUI object using the Create
        # method.
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)
 
        # This next step is the most important, it turns this Python
        # object into the real wrapper of the dialog (instead of pre)
        # as far as the wxPython extension is concerned.
        self.PostCreate(pre)
 
        # This extra style can be set after the UI object has been created.
        if 'wxMac' in wx.PlatformInfo and useMetal:
            self.SetExtraStyle(wx.DIALOG_EX_METAL)
 
 
        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)
  
        label = wx.StaticText(self, -1, u"请输入新增系统基本信息")
        label.SetHelpText("This is the help text for the label")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        self.m_Label_SysName = wx.StaticText(self,wx.ID_ANY, u"系统名称")
        self.m_Text_SysName = wx.TextCtrl(self)
        box.Add(self.m_Label_SysName, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Text_SysName, 3, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_Cyptype = wx.StaticText(self,wx.ID_ANY,u"加密算法")
        sampleList1 = crypt_type_list
        self.m_Choice_Cyptype = wx.Choice(self,choices=sampleList1)
        box.Add(m_Label_Cyptype, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.m_Choice_Cyptype, 3, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_Path = wx.StaticText(self, wx.ID_ANY, u"路径")
        self.text_path = wx.TextCtrl(self)
        button_Path = wx.Button(self, wx.ID_ANY, label="...")
        button_Path.Bind(wx.EVT_BUTTON, self.getPath, button_Path)
        box.Add(m_Label_Path, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.text_path, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(button_Path, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
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

        self.m_Text_SysName.SetValue(self.cur_sys_info.sys_name)
        self.text_path.SetValue(self.cur_sys_info.db_name)
        if self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.md5:
            self.m_Choice_Cyptype.SetSelection(0)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sha1:
            self.m_Choice_Cyptype.SetSelection(1)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.isc:
            self.m_Choice_Cyptype.SetSelection(2)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle10:
            self.m_Choice_Cyptype.SetSelection(3)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.oracle11:
            self.m_Choice_Cyptype.SetSelection(4)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapg:
            self.m_Choice_Cyptype.SetSelection(5)
        elif self.cur_sys_info.db_password_encrypt_algorithm == EncryptAlgorithmType.sapb:
            self.m_Choice_Cyptype.SetSelection(6)

    def getPath(self, evt):
        wx.FileDialog(self)
        file_wildcard = "*.csv"
        dlg = wx.FileDialog(self, "Open csv file...",
                            os.getcwd(),
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.text_path.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OK_button(self, evt):
        if self.m_Text_SysName.GetValue() == "" or self.m_Choice_Cyptype.GetSelection() == -1 or self.cur_sys_info.db_name == "":
            dlg = wx.MessageDialog(None, u"请输入完整信息!", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                #self.Close(True)
                dlg.Destroy()
        else:
            db_util = DBUtil()
            if self.m_Choice_Cyptype.GetSelection() == 0:
                cyp_type = EncryptAlgorithmType.md5
            elif self.m_Choice_Cyptype.GetSelection() == 1:
                cyp_type = EncryptAlgorithmType.sha1
            elif self.m_Choice_Cyptype.GetSelection() == 2:
                cyp_type = EncryptAlgorithmType.isc
            elif self.m_Choice_Cyptype.GetSelection() == 3:
                cyp_type = EncryptAlgorithmType.oracle10
            elif self.m_Choice_Cyptype.GetSelection() == 4:
                cyp_type = EncryptAlgorithmType.oracle11
            elif self.m_Choice_Cyptype.GetSelection() == 5:
                cyp_type = EncryptAlgorithmType.sapg
            elif self.m_Choice_Cyptype.GetSelection() == 6:
                cyp_type = EncryptAlgorithmType.sapb

            self.cur_sys_info.sys_name = self.m_Text_SysName.GetValue()
            self.cur_sys_info.db_name = self.text_path.GetValue()
            self.cur_sys_info.db_password_encrypt_algorithm = cyp_type

            # demo_system = SystemInfo(sys_name=self.m_Text_SysName.GetValue(), db_type=db_type, db_ip=self.m_Text_IP.GetValue(),
            #              db_port=self.m_Text_Port.GetValue(), db_name=self.m_Text_DBname.GetValue(), db_table_name=self.m_Text_Sheetname.GetValue(), db_column_username=self.m_Text_Username.GetValue(),
            #              db_column_password=self.m_Text_Pswname.GetValue(), db_password_encrypt_algorithm=cyp_type)cyp_type
            db_util.update_system(self.cur_sys_info)
            dlg = wx.MessageDialog(None, u"编辑成功!", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
                self.Destroy()
              
    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
            


 


