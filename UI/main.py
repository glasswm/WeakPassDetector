#-*-coding:utf-8-*-
import wx
import wx.lib.masked as masked

#def button
# def bt_start(event):
#     print "IP地址              is  ", m_Text_IP.GetAddress()
#     print "端口                   is  ", m_Text_Port.GetValue()
#     print "数据库类型    is  ", m_Choice_DBType.GetStringSelection()
#     print "加密算法         is  ", m_Choice_Cyptype.GetStringSelection()
#     print "数据库名         is  ", m_Text_DBname.GetValue()
#     print "表名                   is  ", m_Text_Sheetname.GetValue()
#     print "账号字段名    is  ", m_Text_Username.GetValue()
#     print "密码字段名    is  ", m_Text_Pswname.GetValue()
#     m_Text_SumNum.SetValue("801")
#     m_Text_WeakNum.SetValue("80")
#     m_Text_List.SetValue("geng\nhai\nyang\nhello")
    
 
app = wx.App()
win = wx.Frame(None,title="弱口令检测工具",size=(500,600))

bkg = wx.Panel(win)

m_Panel1 = wx.Panel(bkg,wx.ID_ANY)
m_Panel2 = wx.Panel(bkg,wx.ID_ANY)
m_Panel3 = wx.Panel(bkg,wx.ID_ANY)

 
bSizer1 = wx.BoxSizer(wx.VERTICAL)
bSizer1.Add(m_Panel1,proportion=4,flag=wx.EXPAND)
bSizer1.Add(m_Panel2,proportion=1,flag=wx.EXPAND)
bSizer1.Add(m_Panel3,proportion=4,flag=wx.EXPAND)


# m_Label_1 = wx.StaticBox(m_Panel1, label="基本信息")  
# bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_1, wx.HORIZONTAL)  

m_Panel11 = wx.Panel(m_Panel1)
m_Panel12 = wx.Panel(m_Panel1)

bSizer_Panel1 = wx.BoxSizer(wx.HORIZONTAL)
bSizer_Panel1.Add(m_Panel11,proportion=2,flag=wx.EXPAND)
bSizer_Panel1.Add(m_Panel12,proportion=1,flag=wx.EXPAND)
m_Panel1.SetSizer(bSizer_Panel1)

m_Label_11 = wx.StaticBox(m_Panel11, label="系统信息")
bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_11,wx.VERTICAL)


sampleList = ['运维系统','公车系统','管理系统']
listBox = wx.ListBox(m_Panel11,26,wx.DefaultPosition,(300,215),sampleList,wx.LB_SINGLE)
bSizer_Panel11 = wx.BoxSizer(wx.VERTICAL)
bSizer_Panel11.Add(listBox)
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

# m_Label_1 = wx.StaticBox(m_Panel1, label="基本信息")  
# bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_1, wx.HORIZONTAL)  
# 
# 
# m_Panel11 = wx.Panel(m_Panel1)
# m_Panel12 = wx.Panel(m_Panel1)
# bSizer_Panel1 = wx.BoxSizer(wx.HORIZONTAL)
# bSizer_Panel1.Add(m_Panel11,proportion=1,flag=wx.EXPAND)
# bSizer_Panel1.Add(m_Panel12,proportion=1,flag=wx.EXPAND)
# #m_Panel1.SetSizer(bSizer_Panel1)
# 
# bSizerBox_Panel1.Add(bSizer_Panel1,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
# m_Panel1.SetSizer(bSizerBox_Panel1)
# 
# m_Panel111 = wx.Panel(m_Panel11)
# m_Panel112 = wx.Panel(m_Panel11)
# m_Panel113 = wx.Panel(m_Panel11)
# m_Panel114 = wx.Panel(m_Panel11)
# bSizer_Panel11 = wx.BoxSizer(wx.VERTICAL)
# bSizer_Panel11.Add(m_Panel111,proportion=1,flag=wx.EXPAND)
# bSizer_Panel11.Add(m_Panel112,proportion=1,flag=wx.EXPAND)
# bSizer_Panel11.Add(m_Panel113,proportion=1,flag=wx.EXPAND)
# bSizer_Panel11.Add(m_Panel114,proportion=1,flag=wx.EXPAND)
# m_Panel11.SetSizer(bSizer_Panel11)



# listBox = wx.ListBox(m_Panel11,-1,sampleList,wx.LB_SINGLE)
# bSizer_Panel11.Add(listBox)
#m_Panel11.SetSizer(bSizer_Panel11)

# 
# bSizer_Panel11 = wx.StaticBoxSizer(m_Label_11, wx.HORIZONTAL)  
# bSizer_Panel11.Add(listBox,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
# m_Panel11.SetSizer(bSizer_Panel11)


#panel 2
bSizer_Panel2 = wx.BoxSizer(wx.VERTICAL)
m_Panel22 = wx.Panel(m_Panel2)
m_Panel23 = wx.Panel(m_Panel2)

bSizer_Panel2.Add(m_Panel22,proportion=1,flag=wx.EXPAND)
bSizer_Panel2.Add(m_Panel23,proportion=1,flag=wx.EXPAND)
m_Panel2.SetSizer(bSizer_Panel2)



# bSizer_Panel21 = wx.BoxSizer(wx.HORIZONTAL)
# m_Panel211 = wx.Panel(m_Panel21)
# m_Panel212 = wx.Panel(m_Panel21)
# m_Panel213 = wx.Panel(m_Panel21)
# 
# bt_Start = wx.Button(m_Panel212,wx.ID_ANY,label="开始")
# 
# bt_Start.Bind(wx.EVT_BUTTON, bt_start)
# 
# bSizer_Panel212 = wx.BoxSizer(wx.HORIZONTAL)
# bSizer_Panel212.Add(bt_Start,proportion=1,flag=wx.CENTER)
# m_Panel212.SetSizer(bSizer_Panel212)
# 
# bSizer_Panel21.Add(m_Panel211,proportion=1,flag=wx.CENTER)
# bSizer_Panel21.Add(m_Panel212,proportion=1,flag=wx.CENTER)
# bSizer_Panel21.Add(m_Panel213,proportion=1,flag=wx.CENTER)
# 
# m_Panel21.SetSizer(bSizer_Panel21)



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
m_ListCtrl.SetStringItem(0,1,"信息系统 ")

m_ListCtrl.InsertStringItem(1,"hello")
m_ListCtrl.SetStringItem(1,1,"通信系统 ")

#       line = "Line %s" % self.index
#         self.list_ctrl.InsertStringItem(self.index, line)
#         self.list_ctrl.SetStringItem(self.index, 1, "01/19/2010")
#         self.list_ctrl.SetStringItem(self.index, 2, "USA")

bkg.SetSizer(bSizer1) 


win.Show()

app.MainLoop()