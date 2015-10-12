# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 557,357 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel8 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"DBIP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"UserName", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( fgSizer4 )
		self.m_panel8.Layout()
		fgSizer4.Fit( self.m_panel8 )
		gSizer2.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel91 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( self.m_panel91, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer5.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl101 = wx.TextCtrl( self.m_panel91, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl101, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel91, wx.ID_ANY, u"PassWord", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer5.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl111 = wx.TextCtrl( self.m_panel91, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.m_panel91.SetSizer( fgSizer5 )
		self.m_panel91.Layout()
		fgSizer5.Fit( self.m_panel91 )
		gSizer2.Add( self.m_panel91, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer2 )
		self.m_panel4.Layout()
		gSizer2.Fit( self.m_panel4 )
		bSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel12 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Cryptype", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer5.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self.m_panel12, wx.ID_ANY, u"MD5", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		gSizer5.Add( self.m_comboBox2, 0, wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( gSizer5 )
		self.m_panel12.Layout()
		gSizer5.Fit( self.m_panel12 )
		gSizer4.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"SheetName", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		fgSizer7.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl201 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl201, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"DataName", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer7.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		
		self.m_panel13.SetSizer( fgSizer7 )
		self.m_panel13.Layout()
		fgSizer7.Fit( self.m_panel13 )
		gSizer4.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( gSizer4 )
		self.m_panel5.Layout()
		gSizer4.Fit( self.m_panel5 )
		bSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel24 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button2 = wx.Button( self.m_panel24, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.m_panel24.SetSizer( fgSizer9 )
		self.m_panel24.Layout()
		fgSizer9.Fit( self.m_panel24 )
		bSizer4.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer4 )
		self.m_panel6.Layout()
		bSizer4.Fit( self.m_panel6 )
		bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

