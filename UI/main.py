# -*- coding: utf-8 -*-
import  wx
import wx.lib.masked as masked 
from newSysDlg import TestDialog


#---------------------------------------------------------------------------
# Create and set a help provider.  Normally you would do this in
# the app's OnInit as it must be done before any SetHelpText calls.
provider = wx.SimpleHelpProvider()
wx.HelpProvider.Set(provider)
#---------------------------------------------------------------------------
 
class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)
 
 

        m_Panel1 = wx.Panel(self,wx.ID_ANY)
        m_Panel2 = wx.Panel(self,wx.ID_ANY)
        m_Panel3 = wx.Panel(self,wx.ID_ANY)

 
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer1.Add(m_Panel1,proportion=4,flag=wx.EXPAND)
        bSizer1.Add(m_Panel2,proportion=1,flag=wx.EXPAND)
        bSizer1.Add(m_Panel3,proportion=4,flag=wx.EXPAND)


        m_Panel11 = wx.Panel(m_Panel1)
        m_Panel12 = wx.Panel(m_Panel1)

        bSizer_Panel1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel1.Add(m_Panel11,proportion=2,flag=wx.EXPAND)
        bSizer_Panel1.Add(m_Panel12,proportion=1,flag=wx.EXPAND)
        m_Panel1.SetSizer(bSizer_Panel1)

        m_Label_11 = wx.StaticBox(m_Panel11, label="系统信息")
        bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_11,wx.VERTICAL)


        sampleList = ['车辆管理系统','协同办公管理系统','邮件管理系统']
        self.listBox = wx.ListBox(m_Panel11,26,wx.DefaultPosition,(300,215),sampleList,wx.LB_SINGLE)
        bSizer_Panel11 = wx.BoxSizer(wx.VERTICAL)
        bSizer_Panel11.Add(self.listBox)
        bSizerBox_Panel1.Add(bSizer_Panel11,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
        m_Panel11.SetSizer(bSizerBox_Panel1)

        bSizer_Panel12 = wx.BoxSizer(wx.VERTICAL)
        bt_New = wx.Button(m_Panel12,wx.ID_ANY,label="新增系统信息")
        bt_Edit = wx.Button(m_Panel12,wx.ID_ANY,label="编辑系统信息")
        bt_Wstart = wx.Button(m_Panel12,wx.ID_ANY,label="弱口令检测")
        bt_Rstart = wx.Button(m_Panel12,wx.ID_ANY,label="定期修改检测")

        bSizer_Panel12 = wx.GridBagSizer(0,0)
        
        bSizer_Panel12.Add(bt_New, pos=(1, 1), span=(2, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Edit, pos=(4, 1), span=(2, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Wstart, pos=(8, 1), span=(2, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Rstart, pos=(11, 1), span=(2, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.AddGrowableCol(3)
        m_Panel12.SetSizer(bSizer_Panel12)
 
 
         #panel 2
        bSizer_Panel2 = wx.BoxSizer(wx.VERTICAL)
        m_Panel22 = wx.Panel(m_Panel2)
        m_Panel23 = wx.Panel(m_Panel2)
        
        bSizer_Panel2.Add(m_Panel22,proportion=1,flag=wx.EXPAND)
        bSizer_Panel2.Add(m_Panel23,proportion=1,flag=wx.EXPAND)
        m_Panel2.SetSizer(bSizer_Panel2)
        
        m_Panel221 = wx.Panel(m_Panel22)
        m_Panel222 = wx.Panel(m_Panel22)
        
        m_Label_SumNum = wx.StaticText(m_Panel221,wx.ID_ANY,"口令总条数")
        m_Text_SumNum = wx.TextCtrl(m_Panel221)
        m_Label_WeakNum = wx.StaticText(m_Panel222,wx.ID_ANY,"弱口令条数")
        m_Text_WeakNum = wx.TextCtrl(m_Panel222)
        
        bSizer_Panel22 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel22.Add(m_Panel221,proportion=1,flag=wx.EXPAND)
        bSizer_Panel22.Add(m_Panel222,proportion=1,flag=wx.EXPAND)
        m_Panel22.SetSizer(bSizer_Panel22)
        
        bSizer_Panel221 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel221.Add(m_Label_SumNum,proportion=1,flag=wx.LEFT,border=30)
        bSizer_Panel221.Add(m_Text_SumNum,proportion=1,flag=wx.RIGHT,border=30)
        m_Panel221.SetSizer(bSizer_Panel221)
        
        bSizer_Panel222 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel222.Add(m_Label_WeakNum,proportion=1,flag=wx.LEFT,border=30)
        bSizer_Panel222.Add(m_Text_WeakNum,proportion=1,flag=wx.RIGHT,border=30)
        m_Panel222.SetSizer(bSizer_Panel222)
        
        m_Gauge = wx.Gauge(m_Panel23,style = wx.GA_PROGRESSBAR)
        bSizer_Panel23 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel23.Add(m_Gauge,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
        m_Panel23.SetSizer(bSizer_Panel23)
        #panel 3
        #m_Text_List = wx.TextCtrl(m_Panel3)
        # m_Text_List = wx.TextCtrl(m_Panel3,style = wx.TE_MULTILINE)
        m_ListCtrl = wx.ListCtrl(m_Panel3,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        m_ListCtrl.InsertColumn(0,'序号')
        m_ListCtrl.InsertColumn(1,'弱口令用户名')
        m_ListCtrl.InsertColumn(2,'备注')
        # bSizer_Panel3 = wx.BoxSizer(wx.HORIZONTAL)
        # bSizer_Panel3.Add(m_Text_List,proportion = 1,flag=wx.Left|wx.RIGHT|wx.EXPAND)
        m_Label_3 = wx.StaticBox(m_Panel3, label="检测结果")  
        bSizer_Panel3 = wx.StaticBoxSizer(m_Label_3, wx.HORIZONTAL)  
        bSizer_Panel3.Add(m_ListCtrl,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
        m_Panel3.SetSizer(bSizer_Panel3)
        
        m_ListCtrl.InsertStringItem(0,"hello")
        m_ListCtrl.SetStringItem(0,1,"信息系统")
        
        m_ListCtrl.InsertStringItem(1,"hello")
        m_ListCtrl.SetStringItem(1,1,"通信系统")
        
        self.SetSizer(bSizer1) 
        
        self.Bind(wx.EVT_BUTTON, self.NewSysButton, bt_New)
        self.Bind(wx.EVT_BUTTON, self.EditSysButton, bt_Edit)
        

#         b = wx.Button(self, -1, "Create and Show a custom Dialog", (50,50))
#         self.Bind(wx.EVT_BUTTON, self.OnButton, b)
 
#         if 'wxMac' in wx.PlatformInfo:
#             self.cb = wx.CheckBox(self, -1, "Set Metal appearance", (50,90))
 
#     def GetSysInf(): 
#         print("")          
 
    def NewSysButton(self, evt):
        useMetal = False
        if 'wxMac' in wx.PlatformInfo:
            useMetal = self.cb.IsChecked()
             
        dlg = TestDialog(self, -1, "新增系统信息", size=(350, 200),
                         #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                         style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                         useMetal=useMetal,
                         )
        dlg.CenterOnScreen()
 
        # this does not return until the dialog is closed.
        val = dlg.ShowModal()
     
        if val == wx.ID_OK:
            print("You pressed OK\n")
        else:
            print("You pressed Cancel\n")
  
        dlg.Destroy()
        
    def EditSysButton(self, evt):
        print self.listBox.GetStringSelection()
        if self.listBox.GetStringSelection() == '':
            dlg = wx.MessageDialog(None, u"请在右侧选择系统!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
                dlg.Destroy()
        else:
            print("做得好！")
#            GetSysInf()
            
 
def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win
 
 
#---------------------------------------------------------------------------
 
 
overview = """\
wxPython offers quite a few general purpose dialogs for useful data input from
the user; they are all based on the wx.Dialog class, which you can also subclass
to create custom dialogs to suit your needs.
 
The Dialog class, in addition to dialog-like behaviors, also supports the full
wxWindows layout featureset, which means that you can incorporate sizers or
layout constraints as needed to achieve the look and feel desired. It even supports
context-sensitive help, which is illustrated in this example.
 
The example is very simple; in real world situations, a dialog that had input
fields such as this would no doubt be required to deliver those values back to
the calling function. The Dialog class supports data retrieval in this manner.
<b>However, the data must be retrieved prior to the dialog being destroyed.</b>
The example shown here is <i>modal</i>; non-modal dialogs are possible as well.
 
See the documentation for the <code>Dialog</code> class for more details.
 
"""
 
if __name__ == '__main__':
    import sys,os
    #import run
    #run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
    app = wx.App(False)
    frame = wx.Frame(None, -1, '弱口令检测工具',size=(500,600))
    win = TestPanel(frame, None)
    frame.Show()
    app.MainLoop()