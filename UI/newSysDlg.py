# -*- coding: utf-8 -*-
import  wx
import wx.lib.masked as masked 


class TestDialog(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):
 
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
  
        label = wx.StaticText(self, -1, "请输入新增系统基本信息")
        label.SetHelpText("This is the help text for the label")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
  
        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_SysName = wx.StaticText(self,wx.ID_ANY, "系统名称")
        m_Text_SysName = wx.TextCtrl(self)
        box.Add(m_Label_SysName, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_SysName, 3, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
  
        box = wx.BoxSizer(wx.HORIZONTAL)
  
        m_Label_IP = wx.StaticText(self, wx.ID_ANY, "IP地址")
        m_Text_IP = masked.IpAddrCtrl(self, -1, style = wx.TE_PROCESS_TAB)
       
        m_Label_Port = wx.StaticText(self,wx.ID_ANY,"端口号")
        m_Text_Port = wx.TextCtrl(self)
        box.Add(m_Label_IP, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_IP, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Label_Port, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_Port, 2, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_DBType = wx.StaticText(self,wx.ID_ANY,"数据库类型")
        sampleList = ['Oracle', 'mySQL', '其他']
        m_Choice_DBType = wx.Choice(self, choices=sampleList) 
        m_Label_Cyptype = wx.StaticText(self,wx.ID_ANY,"加密算法")
        sampleList1 = ['MD5', 'SHA1', '其他']
        m_Choice_Cyptype = wx.Choice(self,choices=sampleList1)

        box.Add(m_Label_DBType, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Choice_DBType, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Label_Cyptype, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Choice_Cyptype, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_DBname = wx.StaticText(self, wx.ID_ANY, "数据库名")
        m_Text_DBname = wx.TextCtrl(self)
        m_Label_Sheetname = wx.StaticText(self, wx.ID_ANY, "表名")
        m_Text_Sheetname = wx.TextCtrl(self)

        box.Add(m_Label_DBname, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_DBname, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Label_Sheetname, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_Sheetname, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        m_Label_Username = wx.StaticText(self, wx.ID_ANY, "账号字段名")
        m_Text_Username = wx.TextCtrl(self)
        m_Label_Pswname = wx.StaticText(self, wx.ID_ANY, "密码字段名")
        m_Text_Pswname = wx.TextCtrl(self)

        box.Add(m_Label_Username, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_Username, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Label_Pswname, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(m_Text_Pswname, 2, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
  
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
  
        box = wx.BoxSizer(wx.HORIZONTAL)
        bt_Ok = wx.Button(self,wx.ID_ANY,label="确定")
        bt_Cancel = wx.Button(self,wx.ID_ANY,label="取消")
        box.Add(bt_Ok,1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(bt_Cancel,1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
  
        self.SetSizer(sizer)
        sizer.Fit(self)
                
        self.Bind(wx.EVT_BUTTON, self.OK_button, bt_Ok)
        self.Bind(wx.EVT_BUTTON, self.Cancel_Button, bt_Cancel)
        
    def OK_button(self, evt):
        print("ok!")
#         if m_Text_SysName.getText() == '':
#             
#         self.Destroy()
        
    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
            


 
