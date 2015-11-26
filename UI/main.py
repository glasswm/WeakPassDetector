# -*- coding: utf-8 -*-
import  wx
import wx.lib.masked as masked

from ReguTestDlg import ReguTestDialog
from client.common import generate_statement
from client.models import DBUtil
from newSysDlg import NewSysDialog
from editSysDlg import EditSysDialog
from verifDlg import VerifDialog
import logging
from timer import timer


#---------------------------------------------------------------------------
# Create and set a help provider.  Normally you would do this in
# the app's OnInit as it must be done before any SetHelpText calls.
provider = wx.SimpleHelpProvider()
wx.HelpProvider.Set(provider)
#---------------------------------------------------------------------------
class TestPanel(wx.Panel):

    selected_sys = None
    m_Text_SumNum = None
    m_Text_WeakNum = None
    weak_List = None
    username_List = None
    idList = None
    thread = None
    weak_Test = True

    def __init__(self, parent, log):
        self.log = log
        self.idList = []
        wx.Panel.__init__(self, parent, -1)

        m_Panel1 = wx.Panel(self,wx.ID_ANY)
        m_Panel2 = wx.Panel(self,wx.ID_ANY)
        m_Panel3 = wx.Panel(self,wx.ID_ANY)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer1.Add(m_Panel1,proportion=4,flag=wx.EXPAND)
        bSizer1.Add(m_Panel2,proportion=2,flag=wx.EXPAND)
        bSizer1.Add(m_Panel3,proportion=4,flag=wx.EXPAND)

        m_Panel11 = wx.Panel(m_Panel1)
        m_Panel12 = wx.Panel(m_Panel1)
        bSizer_Panel1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel1.Add(m_Panel11,proportion=2,flag=wx.EXPAND)
        bSizer_Panel1.Add(m_Panel12,proportion=1,flag=wx.EXPAND)
        m_Panel1.SetSizer(bSizer_Panel1)

        m_Label_11 = wx.StaticBox(m_Panel11, label=u"系统信息")
        bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_11,wx.VERTICAL)

        self.sampleList = []
        self.listBox = wx.ListBox(m_Panel11,26,wx.DefaultPosition,(300,215),self.sampleList,wx.LB_SINGLE)
        self.RefreshSysList()

        bSizer_Panel11 = wx.BoxSizer(wx.VERTICAL)
        bSizer_Panel11.Add(self.listBox)
        bSizerBox_Panel1.Add(bSizer_Panel11,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
        m_Panel11.SetSizer(bSizerBox_Panel1)
########
        #panel 12-12
        bSizer_Panel12 = wx.BoxSizer(wx.VERTICAL)
        # m_Panel121 = wx.Panel(m_Panel12)
        # m_Panel122 = wx.Panel(m_Panel12)
        # bSizer_Panel12.Add(m_Panel121,proportion=3,flag=wx.EXPAND)
        # bSizer_Panel12.Add(m_Panel122,proportion=2,flag=wx.EXPAND)

        # m_Panel1211 = wx.Panel(m_Panel121)
        # m_Panel1212 = wx.Panel(m_Panel121)
        # m_Panel1213 = wx.Panel(m_Panel121)
        # bSizer_Panel121 = wx.BoxSizer(wx.VERTICAL)
        # bSizer_Panel121.Add(m_Panel1211,proportion=1,flag=wx.EXPAND)
        # bSizer_Panel121.Add(m_Panel1212,proportion=1,flag=wx.EXPAND)
        # bSizer_Panel121.Add(m_Panel1213,proportion=1,flag=wx.EXPAND)

        bt_New = wx.Button(m_Panel12,wx.ID_ANY,label=u"新增系统信息")
        bt_Edit = wx.Button(m_Panel12,wx.ID_ANY,label=u"编辑系统信息")
        bt_Delete = wx.Button(m_Panel12,wx.ID_ANY,label=u"删除系统信息")

        self.bt_Wstart = wx.Button(m_Panel12,wx.ID_ANY,label=u"  弱口令检测 ")
        bt_Export = wx.Button(m_Panel12,wx.ID_ANY,label=u"   导出报表   ")
        #self.bt_Rstart = wx.Button(m_Panel12,wx.ID_ANY,label=u"切换：弱口令检测")

        #m_Label_121 = wx.StaticBox(m_Panel121, label=u"系统维护")
        #m_Label_122 = wx.StaticBox(m_Panel121, label=u"操作类型")
        #bSizerBox_Panel121 = wx.StaticBoxSizer(m_Label_121,wx.VERTICAL)
        #bSizerBox_Panel121.Add(bSizerBox_Panel121,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
        #m_Panel121.SetSizer(bSizerBox_Panel121)
        # bSizerBox_Panel121.Add(bt_New,proportion=1,flag=wx.EXPAND)
        # bSizerBox_Panel121.Add(bt_Edit,proportion=1,flag=wx.EXPAND)
        # bSizerBox_Panel121.Add(bt_Delete,proportion=1,flag=wx.EXPAND)

        #m_Panel121.SetSizer(bSizerBox_Panel121)



        bSizer_Panel12 = wx.GridBagSizer(0,0)

        bSizer_Panel12.Add(bt_New, pos=(1, 1), span=(1, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Edit, pos=(3, 1), span=(1, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Delete, pos=(5, 1), span=(1, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(self.bt_Wstart, pos=(7, 1), span=(1, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.Add(bt_Export, pos=(9, 1), span=(1, 5), flag=wx.ALIGN_CENTER)
        bSizer_Panel12.AddGrowableCol(3)
        m_Panel12.SetSizer(bSizer_Panel12)
 
 
         #panel 2
        bSizer_Panel2 = wx.BoxSizer(wx.VERTICAL)
        m_Panel21 = wx.Panel(m_Panel2)
        m_Panel22 = wx.Panel(m_Panel2)
        m_Panel23 = wx.Panel(m_Panel2)

        bSizer_Panel2.Add(m_Panel21,proportion=1,flag=wx.EXPAND)
        bSizer_Panel2.Add(m_Panel22,proportion=1,flag=wx.EXPAND)
        bSizer_Panel2.Add(m_Panel23,proportion=1,flag=wx.EXPAND)
        m_Panel2.SetSizer(bSizer_Panel2)
        
        # m_Panel221 = wx.Panel(m_Panel22)
        # m_Panel222 = wx.Panel(m_Panel22)
        # m_Panel223 = wx.Panel(m_Panel22)
        self.bt_Stop = wx.Button(m_Panel21,wx.ID_ANY,label=u"停止检测")
        #bt_Export = wx.Button(m_Panel21,wx.ID_ANY,label=u"导出报表")
        self.bt_Rstart = wx.Button(m_Panel21,wx.ID_ANY,label=u"切换模式")
        bSizer_Panel21 = wx.GridBagSizer(2,10)
        bSizer_Panel21.Add(self.bt_Rstart, pos=(0,6), span=(1,3), flag = wx.ALIGN_CENTER)
        bSizer_Panel21.Add(self.bt_Stop, pos=(0,11), span=(1,3), flag = wx.ALIGN_CENTER)
        m_Panel21.SetSizer(bSizer_Panel21)

        m_Label_SumNum = wx.StaticText(m_Panel22,wx.ID_ANY,u"口令总条数")
        self.m_Text_SumNum = wx.TextCtrl(m_Panel22,size=(50,22))
        self.m_Text_SumNum.SetEditable(False)
        m_Label_WeakNum = wx.StaticText(m_Panel22,wx.ID_ANY,u"弱口令条数")
        self.m_Text_WeakNum = wx.TextCtrl(m_Panel22,size=(50,22))
        print self.m_Text_WeakNum.GetSize()
        self.m_Text_WeakNum.SetEditable(False)
        m_Label_UnknownNum = wx.StaticText(m_Panel22,wx.ID_ANY,u"不明口令条数")
        self.m_Text_UnknownNum = wx.TextCtrl(m_Panel22,size=(50,22))
        self.m_Text_UnknownNum.SetEditable(False)

        bSizer_Panel22 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel22 = wx.GridBagSizer(2,10)

        bSizer_Panel22.Add(m_Label_SumNum, pos=(0, 2), span=(1, 1), flag=wx.ALIGN_CENTER)
        bSizer_Panel22.Add(self.m_Text_SumNum, pos=(0, 3), span=(1, 1), flag=wx.ALIGN_CENTER)
        bSizer_Panel22.Add(m_Label_WeakNum, pos=(0, 4), span=(1, 1), flag=wx.ALIGN_CENTER)
        bSizer_Panel22.Add(self.m_Text_WeakNum, pos=(0, 5), span=(1, 1), flag=wx.ALIGN_CENTER)
        bSizer_Panel22.Add(m_Label_UnknownNum, pos=(0, 6), span=(1, 1), flag=wx.ALIGN_CENTER)
        bSizer_Panel22.Add(self.m_Text_UnknownNum, pos=(0, 7), span=(1, 1), flag=wx.ALIGN_CENTER)

        #bSizer_Panel12.AddGrowableCol(3)
        m_Panel22.SetSizer(bSizer_Panel22)

        # bSizer_Panel22.Add(m_Panel221,proportion=1,flag=wx.EXPAND)
        # bSizer_Panel22.Add(m_Panel222,proportion=1,flag=wx.EXPAND)
        # bSizer_Panel22.Add(m_Panel223,proportion=1,flag=wx.EXPAND)
        # m_Panel22.SetSizer(bSizer_Panel22)
        
        # bSizer_Panel221 = wx.BoxSizer(wx.HORIZONTAL)
        # bSizer_Panel221.Add(m_Label_SumNum,proportion=0.3)
        # bSizer_Panel221.Add(self.m_Text_SumNum,proportion=0.3)
        # m_Panel221.SetSizer(bSizer_Panel221)
        #
        # bSizer_Panel222 = wx.BoxSizer(wx.HORIZONTAL)
        # bSizer_Panel222.Add(m_Label_WeakNum,proportion=0.5,flag=wx.LEFT)
        # bSizer_Panel222.Add(self.m_Text_WeakNum,proportion=0.5,flag=wx.RIGHT)
        # m_Panel222.SetSizer(bSizer_Panel222)
        #
        # bSizer_Panel223 = wx.BoxSizer(wx.HORIZONTAL)
        # bSizer_Panel223.Add(m_Label_UnknownNum,proportion=0.5,flag=wx.LEFT)
        # bSizer_Panel223.Add(self.m_Text_UnknownNum,proportion=0.5,flag=wx.RIGHT)
        # m_Panel223.SetSizer(bSizer_Panel223)
        
        self.m_Gauge = wx.Gauge(m_Panel23,style = wx.GA_PROGRESSBAR)
        self.count = 0
        bSizer_Panel23 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_Panel23.Add(self.m_Gauge,proportion=1,flag=wx.LEFT|wx.RIGHT,border=10)
        m_Panel23.SetSizer(bSizer_Panel23)
        #self.m_Gauge.Bind(wx.wxEVT_IDLE,self.OnIdle)
        #panel 3
        #m_Text_List = wx.TextCtrl(m_Panel3)
        # m_Text_List = wx.TextCtrl(m_Panel3,style = wx.TE_MULTILINE)
        self.m_ListCtrl = wx.ListCtrl(m_Panel3,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.m_ListCtrl.InsertColumn(0,u'序号',wx.LIST_FORMAT_CENTER)
        self.m_ListCtrl.SetColumnWidth(0, 70)
        self.m_ListCtrl.InsertColumn(1,u'弱口令用户名',wx.LIST_FORMAT_CENTER)
        self.m_ListCtrl.SetColumnWidth(1, 300)
        self.m_ListCtrl.InsertColumn(2,u'备注',wx.LIST_FORMAT_CENTER)
        # bSizer_Panel3 = wx.BoxSizer(wx.HORIZONTAL)
        # bSizer_Panel3.Add(m_Text_List,proportion = 1,flag=wx.Left|wx.RIGHT|wx.EXPAND)
        m_Label_3 = wx.StaticBox(m_Panel3, label=u"检测结果")  
        bSizer_Panel3 = wx.StaticBoxSizer(m_Label_3, wx.HORIZONTAL)  
        bSizer_Panel3.Add(self.m_ListCtrl,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
        m_Panel3.SetSizer(bSizer_Panel3)

        self.SetSizer(bSizer1) 
        
        self.Bind(wx.EVT_BUTTON, self.NewSysButton, bt_New)
        self.Bind(wx.EVT_BUTTON, self.EditSysButton, bt_Edit)
        self.Bind(wx.EVT_BUTTON, self.TestStartButton, self.bt_Wstart)
        self.Bind(wx.EVT_BUTTON, self.DeleteSysButton, bt_Delete)
        self.Bind(wx.EVT_BUTTON, self.ExportReport, bt_Export)
        self.Bind(wx.EVT_BUTTON, self.StopTest, self.bt_Stop)
        self.Bind(wx.EVT_BUTTON, self.ModeSwitchButton, self.bt_Rstart)

    def NewSysButton(self, evt):
        useMetal = False
        if 'wxMac' in wx.PlatformInfo:
            useMetal = self.cb.IsChecked()
             
        dlg = NewSysDialog(self, -1, u"新增系统信息", size=(350, 200),
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
            dlg = wx.MessageDialog(None, u"请在左侧选择系统!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                #self.Close(True)
                dlg.Destroy()
        else:
            print(u"做得好！")
            useMetal = False
            if 'wxMac' in wx.PlatformInfo:
                useMetal = self.cb.IsChecked()
            dlg = EditSysDialog(self, -1, u"编辑系统信息", idx=self.idList[self.listBox.GetSelection()], size=(350, 200),
                             style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                             useMetal=useMetal
                             )
            dlg.CenterOnScreen()
            val = dlg.ShowModal()
     
            if val == wx.ID_OK:
                print("You pressed OK\n")
            else:
                print("You pressed Cancel\n")
  
            dlg.Destroy()

    def DeleteSysButton(self, evt):
        print self.listBox.GetStringSelection()
        if self.listBox.GetStringSelection() == '':
            dlg = wx.MessageDialog(None, u"请在左侧选择系统!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                #self.Close(True)
                dlg.Destroy()
        else:
            useMetal = False
            if 'wxMac' in wx.PlatformInfo:
                useMetal = self.cb.IsChecked()
            dlg = wx.MessageDialog(None, u"确定删除此系统？", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                print "delete that system"
                print self.listBox.GetSelection()
                db_util = DBUtil()
                print self.idList
                db_util.del_system_by_id(self.idList[self.listBox.GetSelection()])
                self.RefreshSysList()
            dlg.Destroy()

    def TestStartButton(self,evt):
        if self.weak_Test == True:
            self.WeakCheckStartButton()
        else:
            self.RegularModifyTestButton()

    def ModeSwitchButton(self,evt):
        print self.listBox.GetStringSelection()
        self.weak_Test = 1 - self.weak_Test
        print self.weak_Test
        if self.weak_Test == True:
            self.bt_Wstart.SetLabel("弱口令检测".decode('utf-8'))
        else:
            self.bt_Wstart.SetLabel("定期修改检测".decode('utf-8'))

    def WeakCheckStartButton(self):
        print self.listBox.GetStringSelection()
        if self.listBox.GetStringSelection() == '':
            dlg = wx.MessageDialog(None, u"请在左侧选择系统!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            useMetal = False
            if 'wxMac' in wx.PlatformInfo:
                useMetal = self.cb.IsChecked()

            self.thread = timer(self, idx=self.idList[self.listBox.GetSelection()])
            dlg = VerifDialog(self, -1, u"输入口令", idx=self.idList[self.listBox.GetSelection()], size=(350, 200),
                              style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                              useMetal=useMetal,
                              )
            dlg.CenterOnScreen()
            val = dlg.ShowModal()
            if val == wx.ID_OK:
                print("You pressed OK\n")
            else:
                print("You pressed Cancel\n")
            dlg.Destroy()

    def RegularModifyTestButton(self):
        # self.m_ListCtrl.DeleteColumn(1)
        # self.m_ListCtrl.InsertColumn(1,u'xxxx',wx.LIST_FORMAT_CENTER)
        if self.listBox.GetStringSelection() == '':
            dlg = wx.MessageDialog(None, u"请在左侧选择系统!", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            useMetal = False
            if 'wxMac' in wx.PlatformInfo:
                useMetal = self.cb.IsChecked()

            dlg = ReguTestDialog(self, -1, u"输入口令", idx=self.idList[self.listBox.GetSelection()], size=(350, 200),
                              style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                              useMetal=useMetal,
                              )
            dlg.CenterOnScreen()
            val = dlg.ShowModal()
            if val == wx.ID_OK:
                print("You pressed OK\n")
            else:
                print("You pressed Cancel\n")
            dlg.Destroy()

    def OnIdle(self):
        self.gauge.SetValue(self.count)

    def RefreshSysList(self):
        self.listBox.Clear()
        self.sampleList = []
        db_util = DBUtil()
        res = []
        self.idList = []
        res = db_util.get_all_system()
        print ("length of res")
        print(len(res))
        for i in res:
            self.sampleList.append(i.sys_name)
            self.idList.append(i.id)
        print self.idList
        self.listBox.SetItems(self.sampleList)

    def ExportReport(self, evt):
        if self.weak_Test == True:
            self.WeakTestReport()
        else:
            self.RegularTestReport()

    def WeakTestReport(self):
        print ("export report")
        wl = []
        for i in self.weak_List:
            temp = {'name' : 'aaaa1', 'wtype' : '1'}
            temp['name'] = self.username_List[i]
            wl.append(temp)
        generate_statement(self.listBox.GetStringSelection(), u'汪明', wl, self.m_Text_SumNum.GetValue(), self.m_Text_WeakNum.GetValue())

    def RegularTestReport(self):
        print("regular test report")

    def StopTest(self, evt):
        print ("stop testing, stop thread")
        self.thread.stop()
        #self.thread.join()

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
    frame = wx.Frame(None, -1, u'弱口令检测工具',size=(500,600))
    win = TestPanel(frame, None)
    frame.Show()
    app.MainLoop()