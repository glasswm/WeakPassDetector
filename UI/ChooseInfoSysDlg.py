# -*- coding: utf-8 -*-
from time import sleep
import  wx
from newSysDlg import NewSysDialog
from newSysDlg2 import NewSysDialog2

class ChooseInfoSysDlg(wx.Dialog):

    cur_sys_info = None
    parent = None
    isFromFile = False
    useMetal = False

    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE,
            useMetal=False,
            ):
        self.parent = parent
        self.useMetal = useMetal
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
        lblList = [u'从数据库中创建', u'从文件中创建']
        self.m_info_sys_file = wx.RadioBox(self, label = u'选择信息系统来源', pos = (80,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.m_info_sys_file.Bind(wx.EVT_RADIOBOX,self.onRadioBox)
        box.Add(self.m_info_sys_file, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

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

    def onRadioBox(self,e):
        print self.m_info_sys_file.GetStringSelection(),' is clicked from Radio Box'
        if self.m_info_sys_file.GetSelection() == 1:
            self.isFromFile = True

    def OK_button(self, evt):
        print self.isFromFile
        if self.isFromFile:
            dlg = NewSysDialog2(self, -1, u"新增信息系统", size=(350, 200),
                 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                 useMetal = self.useMetal,
                 )
            dlg.CenterOnScreen()
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = NewSysDialog(self, -1, u"新增信息系统", size=(350, 200),
                 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                 useMetal = self.useMetal,
                 )
            dlg.CenterOnScreen()
            dlg.ShowModal()
            dlg.Destroy()

        self.Destroy()

    def Cancel_Button(self, evt):
        print("cancel!")
        self.Destroy()
