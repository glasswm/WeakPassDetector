#-*-coding:utf-8-*-
import wx
import wx.lib.masked as masked

#def button
def bt_start(event):
    print "IP地址              is  ", m_Text_IP.GetAddress()
    print "端口                   is  ", m_Text_Port.GetValue()
    print "数据库类型    is  ", m_Choice_DBType.GetStringSelection()
    print "加密算法         is  ", m_Choice_Cyptype.GetStringSelection()
    print "数据库名         is  ", m_Text_DBname.GetValue()
    print "表名                   is  ", m_Text_Sheetname.GetValue()
    print "账号字段名    is  ", m_Text_Username.GetValue()
    print "密码字段名    is  ", m_Text_Pswname.GetValue()
    m_Text_SumNum.SetValue("801")
    m_Text_WeakNum.SetValue("80")
    m_Text_List.SetValue("geng\nhai\nyang\nhello")
    
 
app = wx.App()
win = wx.Frame(None,title="弱口令检测工具",size=(500,600))

bkg = wx.Panel(win)

m_Panel1 = wx.Panel(bkg,wx.ID_ANY)
m_Panel2 = wx.Panel(bkg,wx.ID_ANY)
m_Panel3 = wx.Panel(bkg,wx.ID_ANY)

 
bSizer1 = wx.BoxSizer(wx.VERTICAL)
bSizer1.Add(m_Panel1,proportion=2,flag=wx.EXPAND)
bSizer1.Add(m_Panel2,proportion=1,flag=wx.EXPAND)
bSizer1.Add(m_Panel3,proportion=2,flag=wx.EXPAND)


m_Label_1 = wx.StaticBox(m_Panel1, label="基本信息")  
bSizerBox_Panel1 = wx.StaticBoxSizer(m_Label_1, wx.HORIZONTAL)  


m_Panel11 = wx.Panel(m_Panel1)
m_Panel12 = wx.Panel(m_Panel1)
bSizer_Panel1 = wx.BoxSizer(wx.HORIZONTAL)
bSizer_Panel1.Add(m_Panel11,proportion=1,flag=wx.EXPAND)
bSizer_Panel1.Add(m_Panel12,proportion=1,flag=wx.EXPAND)
#m_Panel1.SetSizer(bSizer_Panel1)

bSizerBox_Panel1.Add(bSizer_Panel1,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
m_Panel1.SetSizer(bSizerBox_Panel1)

m_Panel111 = wx.Panel(m_Panel11)
m_Panel112 = wx.Panel(m_Panel11)
m_Panel113 = wx.Panel(m_Panel11)
m_Panel114 = wx.Panel(m_Panel11)
bSizer_Panel11 = wx.BoxSizer(wx.VERTICAL)
bSizer_Panel11.Add(m_Panel111,proportion=1,flag=wx.EXPAND)
bSizer_Panel11.Add(m_Panel112,proportion=1,flag=wx.EXPAND)
bSizer_Panel11.Add(m_Panel113,proportion=1,flag=wx.EXPAND)
bSizer_Panel11.Add(m_Panel114,proportion=1,flag=wx.EXPAND)
m_Panel11.SetSizer(bSizer_Panel11)

bSizer_Panel111 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_IP = wx.StaticText(m_Panel111, wx.ID_ANY, "IP地址")
#m_Text_IP = wx.TextCtrl(m_Panel111)
m_Text_IP = masked.IpAddrCtrl(m_Panel111, -1, style = wx.TE_PROCESS_TAB)


bSizer_Panel111.Add(m_Label_IP,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel111.Add(m_Text_IP,proportion=1,flag=wx.RIGHT)
m_Panel111.SetSizer(bSizer_Panel111)

bSizer_Panel112 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_Port = wx.StaticText(m_Panel112,wx.ID_ANY,"端口号")
m_Text_Port = wx.TextCtrl(m_Panel112)
bSizer_Panel112.Add(m_Label_Port,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel112.Add(m_Text_Port,proportion=1,flag=wx.RIGHT)
m_Panel112.SetSizer(bSizer_Panel112)

bSizer_Panel113 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_DBType = wx.StaticText(m_Panel113,wx.ID_ANY,"数据库类型")
#m_List_Cypt = wx.TextCtrl(m_Panel113)
sampleList = ['Oracle', 'mySQL', '其他']
m_Choice_DBType = wx.Choice(m_Panel113, choices=sampleList) 

bSizer_Panel113.Add(m_Label_DBType,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel113.Add(m_Choice_DBType,proportion=1,flag=wx.RIGHT)
m_Panel113.SetSizer(bSizer_Panel113)

bSizer_Panel114 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_Cyptype = wx.StaticText(m_Panel114,wx.ID_ANY,"加密算法")
#m_Listbox_Cyptype = wx.ListBox(m_Panel114)
sampleList1 = ['MD5', 'SHA1', '其他']
m_Choice_Cyptype = wx.Choice(m_Panel114,choices=sampleList1)
bSizer_Panel114.Add(m_Label_Cyptype,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel114.Add(m_Choice_Cyptype,proportion=1,flag=wx.RIGHT)
m_Panel114.SetSizer(bSizer_Panel114)

m_Panel121 = wx.Panel(m_Panel12)
m_Panel122 = wx.Panel(m_Panel12)
m_Panel123 = wx.Panel(m_Panel12)
m_Panel124 = wx.Panel(m_Panel12)

bSizer_Panel12 = wx.BoxSizer(wx.VERTICAL)
bSizer_Panel12.Add(m_Panel121,proportion=1,flag=wx.EXPAND)
bSizer_Panel12.Add(m_Panel122,proportion=1,flag=wx.EXPAND)
bSizer_Panel12.Add(m_Panel123,proportion=1,flag=wx.EXPAND)
bSizer_Panel12.Add(m_Panel124,proportion=1,flag=wx.EXPAND)
m_Panel12.SetSizer(bSizer_Panel12)

bSizer_Panel121 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_DBname = wx.StaticText(m_Panel121, wx.ID_ANY, "数据库名")
m_Text_DBname = wx.TextCtrl(m_Panel121)
bSizer_Panel121.Add(m_Label_DBname,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel121.Add(m_Text_DBname,proportion=1,flag=wx.RIGHT,border=10)
m_Panel121.SetSizer(bSizer_Panel121)

bSizer_Panel122 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_Sheetname = wx.StaticText(m_Panel122, wx.ID_ANY, "表名")
m_Text_Sheetname = wx.TextCtrl(m_Panel122)
bSizer_Panel122.Add(m_Label_Sheetname,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel122.Add(m_Text_Sheetname,proportion=1,flag=wx.RIGHT,border=10)
m_Panel122.SetSizer(bSizer_Panel122)

bSizer_Panel123 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_Username = wx.StaticText(m_Panel123, wx.ID_ANY, "账号字段名")
m_Text_Username = wx.TextCtrl(m_Panel123)
bSizer_Panel123.Add(m_Label_Username,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel123.Add(m_Text_Username,proportion=1,flag=wx.RIGHT,border=10)
m_Panel123.SetSizer(bSizer_Panel123)

bSizer_Panel124 = wx.BoxSizer(wx.HORIZONTAL)
m_Label_Pswname = wx.StaticText(m_Panel124, wx.ID_ANY, "密码字段名")
m_Text_Pswname = wx.TextCtrl(m_Panel124)
bSizer_Panel124.Add(m_Label_Pswname,proportion=1,flag=wx.LEFT,border=10)
bSizer_Panel124.Add(m_Text_Pswname,proportion=1,flag=wx.RIGHT,border=10)
m_Panel124.SetSizer(bSizer_Panel124)

#line = wx.StaticLine(m_Panel1)


#panel 2
bSizer_Panel2 = wx.BoxSizer(wx.VERTICAL)
m_Panel21 = wx.Panel(m_Panel2)
m_Panel22 = wx.Panel(m_Panel2)
m_Panel23 = wx.Panel(m_Panel2)
bSizer_Panel2.Add(m_Panel21,proportion=1,flag=wx.EXPAND)
bSizer_Panel2.Add(m_Panel22,proportion=1,flag=wx.EXPAND)
bSizer_Panel2.Add(m_Panel23,proportion=1,flag=wx.EXPAND)
m_Panel2.SetSizer(bSizer_Panel2)


bSizer_Panel21 = wx.GridBagSizer(0,0)
bt_Start = wx.Button(m_Panel21,wx.ID_ANY,label="开始")
bSizer_Panel21.Add(bt_Start, pos=(0, 0), span=(1, 5), flag=wx.ALIGN_CENTER)
bSizer_Panel21.AddGrowableCol(4)
m_Panel21.SetSizer(bSizer_Panel21)
# bSizer_Panel21 = wx.BoxSizer(wx.HORIZONTAL)
# m_Panel211 = wx.Panel(m_Panel21)
# m_Panel212 = wx.Panel(m_Panel21)
# m_Panel213 = wx.Panel(m_Panel21)
# 
# bt_Start = wx.Button(m_Panel212,wx.ID_ANY,label="开始")
# 
bt_Start.Bind(wx.EVT_BUTTON, bt_start)
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
m_Text_List = wx.TextCtrl(m_Panel3,style = wx.TE_MULTILINE)
# bSizer_Panel3 = wx.BoxSizer(wx.HORIZONTAL)
# bSizer_Panel3.Add(m_Text_List,proportion = 1,flag=wx.Left|wx.RIGHT|wx.EXPAND)
m_Label_3 = wx.StaticBox(m_Panel3, label="检测结果")  
bSizer_Panel3 = wx.StaticBoxSizer(m_Label_3, wx.HORIZONTAL)  
bSizer_Panel3.Add(m_Text_List,proportion = 5,flag=wx.LEFT|wx.RIGHT |wx.EXPAND, border=10)
m_Panel3.SetSizer(bSizer_Panel3)



bkg.SetSizer(bSizer1) 


win.Show()

app.MainLoop()