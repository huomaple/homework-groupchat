# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import wx.aui
import socket
import threading
import time
import struct
import re
import hashlib
import os

###########################################################################
## Class MainLayout
###########################################################################

class LoginLayout ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"登录界面", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		LoginDesign = wx.BoxSizer( wx.VERTICAL )
		
		LoginDesign.SetMinSize( wx.Size( 400,300 ) ) 
		Lg = wx.BoxSizer( wx.VERTICAL )
		
		Lg.SetMinSize( wx.Size( 400,300 ) ) 
		LgName = wx.BoxSizer( wx.HORIZONTAL )
		
		LgName.SetMinSize( wx.Size( 300,100 ) ) 
		self.StatLgName = wx.StaticText( self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatLgName.Wrap( -1 )
		LgName.Add( self.StatLgName, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.InputName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,25 ), 0 )
		LgName.Add( self.InputName, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		Lg.Add( LgName, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		LgAddr = wx.BoxSizer( wx.HORIZONTAL )
		
		LgAddr.SetMinSize( wx.Size( 300,50 ) ) 
		self.StatLgAddr = wx.StaticText( self, wx.ID_ANY, u"地址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatLgAddr.Wrap( -1 )
		LgAddr.Add( self.StatLgAddr, 0, wx.ALL, 5 )
		
		self.InputAddr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,25 ) , 0 )
		self.InputAddr.SetValue("119.28.133.55")
		LgAddr.Add( self.InputAddr, 0, wx.ALL, 5 )
		
		
		Lg.Add( LgAddr, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		LgButon = wx.BoxSizer( wx.HORIZONTAL )
		
		LgButon.SetMinSize( wx.Size( 400,100 ) ) 
		LayoutLg = wx.BoxSizer( wx.VERTICAL )
		
		self.LoginBt = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayoutLg.Add( self.LoginBt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		LgButon.Add( LayoutLg, 1, wx.EXPAND, 5 )
		
		LayoutEx = wx.BoxSizer( wx.VERTICAL )
		
		self.ExitBt = wx.Button( self, wx.ID_ANY, u"退出", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		LayoutEx.Add( self.ExitBt, 0, wx.ALL, 5 )
		
		
		LgButon.Add( LayoutEx, 1, wx.EXPAND, 5 )
		
		
		Lg.Add( LgButon, 0, 0, 5 )
		
		
		LoginDesign.Add( Lg, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( LoginDesign )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.LoginBt.Bind( wx.EVT_BUTTON, self.Loginon )
		self.ExitBt.Bind( wx.EVT_BUTTON, self.Exit )
	
	def __del__( self ):
		pass

	def Loginon( self, event ): 
		Name = self.InputName.GetValue()
		Address = self.InputAddr.GetValue()
		if Name != "" and Address != "":
			port = 23334 #接口选择大于10000的，避免冲突
			bufsize = 1024  #定义缓冲大小
			addr = (Address,port) # 元祖形式
			self.tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

			try:
				self.tcpClient.connect(addr)
				self.tcpClient.sendall(Name.encode(encoding = 'utf-8'))
				self.Main = MainLayout( self.GetParent() ,"昵称:" + Name + "  与" + Address + "连接中 " , Name)

				t2 = receM()
				t2.setDaemon(True)
				t2.start()

				t3 = loginlist()
				t3.setDaemon(True)
				t3.start()

				self.Destroy()
				self.Main.Show(True)
			except Exception as e:
				dlg = wx.MessageDialog(None, "连接失败", "警告", wx.YES_NO | wx.ICON_QUESTION)
				if dlg.ShowModal() == wx.ID_YES:
					self.Close(True)
				dlg.Destroy()
				event.Skip()
		
	
	def Exit( self, event ):
		self.Destroy()
	
class MainLayout ( wx.Frame ):
	
	def __init__( self, parent ,title1 , tName):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY ,title = title1 ,pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.tName = tName
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainDesign = wx.BoxSizer( wx.VERTICAL )
		
		MainDesign.SetMinSize( wx.Size( 600,600 ) ) 
		tL = wx.BoxSizer( wx.HORIZONTAL )
		
		tL.SetMinSize( wx.Size( 600,400 ) ) 
		self.TalkList = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,400 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS|wx.TE_READONLY )
		self.TalkList.SetMinSize( wx.Size( 400,400 ) )
		self.TalkList.SetMaxSize( wx.Size( 400,400 ) )
		
		tL.Add( self.TalkList, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.OnlinePL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,200 ), 0|wx.TE_MULTILINE )
		bSizer14.Add( self.OnlinePL, 0, wx.ALL, 5 )
		
		self.FileList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), 0|wx.TE_MULTILINE )
		bSizer14.Add( self.FileList, 0, wx.ALL, 5 )
		
		self.FileDown = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer14.Add( self.FileDown, 0, wx.ALL, 5 )
		
		self.DownLoadButton = wx.Button( self, wx.ID_ANY, "下载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.DownLoadButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		tL.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		MainDesign.Add( tL, 1, wx.EXPAND, 5 )
		
		Wl = wx.BoxSizer( wx.HORIZONTAL )
		
		Wl.SetMinSize( wx.Size( 600,200 ) ) 
		TbnWl = wx.BoxSizer( wx.VERTICAL )
		
		TbnWl.SetMinSize( wx.Size( 600,200 ) ) 
		self.Edit = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,170 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.Edit.SetMinSize( wx.Size( 600,170 ) )
		self.Edit.SetMaxSize( wx.Size( 600,170 ) )
		
		TbnWl.Add( self.Edit, 1, wx.ALL, 5 )
		
		TnB = wx.BoxSizer( wx.HORIZONTAL )
		
		TnB.SetMinSize( wx.Size( 600,30 ) ) 
		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,30 ), wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_auiToolBar1.SetMinSize( wx.Size( 400,30 ) )
		self.m_auiToolBar1.SetMaxSize( wx.Size( 400,30 ) )
		
		self.Emoji = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool",   wx.Bitmap(wx.Image('emoji/emoji_head.jpg', wx.BITMAP_TYPE_ANY)), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.File = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap(wx.Image('emoji/file.jpg', wx.BITMAP_TYPE_ANY)), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.Realize() 
		
		TnB.Add( self.m_auiToolBar1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer19.SetMinSize( wx.Size( 200,30 ) ) 
		self.AnswerButton = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.AnswerButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		TnB.Add( bSizer19, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		TbnWl.Add( TnB, 0, wx.ALL, 5 )
		
		
		Wl.Add( TbnWl, 0, 0, 5 )
		
		
		MainDesign.Add( Wl, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( MainDesign )
		self.Layout()
		
		self.Centre( wx.BOTH )


		t1 = sendM()
		t1.setDaemon(True)
			
		# Connect Events
		self.AnswerButton.Bind( wx.EVT_BUTTON, t1.start )
		self.DownLoadButton.Bind( wx.EVT_BUTTON, self.DownLoad)
		self.Bind( wx.EVT_TOOL, self.emojiadd, id = self.Emoji.GetId() )
		self.Bind( wx.EVT_TOOL, self.uploadfile, id = self.File.GetId() )

		self.flag = 0
	
	def __del__( self ):
		pass

	def emojiadd (self , event):
		if self.flag == 0:
			self.panel = MyPanel1( frame.Main )
			self.panel.Show(True)
			self.flag = 1
		else:
			self.panel.Destroy()
			self.flag = 0
	
	def DownLoad(self , event):
		filename = frame.Main.FileDown.GetValue()
		frame.Main.FileDown.Clear()
		t4 = FileTcp()
		t4.set_type('0')
		t4.set_filename(filename)
		t4.start()

	def uploadfile(self , event):
		self.up = MyDialog1( frame.Main )
		self.up.Show(True)

class MyDialog1 ( wx.Dialog ):
    	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"文件路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"上传", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetLabel("上传进度条：0%")
		bSizer6.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.upload )
		self.m_button2.Bind( wx.EVT_BUTTON, self.quit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def upload( self, event ):
		filepath = self.m_textCtrl1.GetValue()
		if filepath !='':
			t4 = FileTcp()
			t4.set_type('1')
			t4.set_filepath(filepath)
			t4.start()
    		
	
	def quit( self, event ):
		self.Destroy()

class FileTcp(threading.Thread):
	BUFFER_SIZE = 1024
	HEAD_STRUCT = '128sIq32s'
	info_size = struct.calcsize(HEAD_STRUCT)

	def __init__( self, *args, **kwargs):
		super(FileTcp, self).__init__(*args, **kwargs)
	
	def run(self):
		if self.type == '0':
			print("downloading")
			FileTcp.recv_file(self, self.filename)
		else:
			print("uploading")
			FileTcp.send_file(self, self.filepath)
    		

	def set_filename(self, filename):
		self.filename = filename

	def set_filepath(self, filepath):
		self.filepath = filepath

	def set_type(self , type):
		self.type = type
    	
	def cal_md5(file_path):
		with open(file_path, 'rb') as fr:
			md5 = hashlib.md5()
			md5.update(fr.read())
			md5 = md5.hexdigest()
		return md5

	def unpack_file_info(file_info):
		file_name, file_name_len, file_size, md5 = struct.unpack(FileTcp.HEAD_STRUCT, file_info)
		file_name = file_name.decode(encoding = 'utf-8')
		md5 = md5.decode(encoding = 'utf-8')
		file_name = file_name[:file_name_len]
		return file_name, file_size, md5


	def recv_file(self , filename):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = ('119.28.133.55', 23336)

		sock.connect(server_address)
		sock.sendall(self.type.encode(encoding = 'utf-8'))
		time.sleep(0.01)
		sock.sendall(filename.encode(encoding = 'utf-8'))

		file_info_package = sock.recv(FileTcp.info_size)
		file_name, file_size, md5_recv = FileTcp.unpack_file_info(file_info_package)

		recved_size = 0
		with open(file_name, 'wb') as fw:
			while recved_size < file_size:
				
				remained_size = file_size - recved_size
				recv_size = 0
				if remained_size > FileTcp.BUFFER_SIZE :
					recv_size = FileTcp.BUFFER_SIZE 
				else :
					recv_size = remained_size
				recv_file = sock.recv(recv_size)
				recved_size += recv_size
				fw.write(recv_file)
		md5 = FileTcp.cal_md5(file_name)
		if md5 != md5_recv:
			dlg = wx.MessageDialog(None, "MD5校验错误，下载失败", "警告", wx.YES_NO | wx.ICON_QUESTION)
			if dlg.ShowModal() == wx.ID_YES:
				dlg.Close(True)
			dlg.Destroy()
		else:
			dlg = wx.MessageDialog(None, "下载成功", "提醒", wx.YES_NO | wx.ICON_QUESTION)
			if dlg.ShowModal() == wx.ID_YES:
				dlg.Close(True)
			dlg.Destroy()
		sock.close()

	def get_file_info(file_path):
		file_name = os.path.basename(file_path)
		file_name_len = len(file_name)
		file_size = os.path.getsize(file_path)
		md5 = FileTcp.cal_md5(file_path)
		return file_name, file_name_len, file_size, md5


	def send_file(self, file_path):
		file_name, file_name_len, file_size, md5 = FileTcp.get_file_info(file_path)
		file_head = struct.pack(FileTcp.HEAD_STRUCT, file_name.encode(encoding = 'utf-8'), file_name_len, file_size, md5.encode(encoding = 'utf-8'))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = ('119.28.133.55', 23336)

		sock.connect(server_address)
		try:
			sock.sendall(self.type.encode(encoding = 'utf-8'))
			time.sleep(0.01)
			sock.sendall(file_head)
			sent_size = 0

			with open(file_path , 'rb') as fr:
				while sent_size < file_size:
					remained_size = file_size - sent_size
					send_size = 0
					if remained_size > FileTcp.BUFFER_SIZE :
						send_size = FileTcp.BUFFER_SIZE
					else :
						send_size = remained_size
					send_file = fr.read(send_size)
					sent_size += send_size
					sock.sendall(send_file)
					frame.Main.up.m_staticText3.SetLabel("上传进度条："+str((sent_size/file_size)*100)+"%")
					time.sleep(0.2)
		except Exception as e:
			pass
		finally:
			flag = sock.recv(1)
			flag = flag.decode(encoding = 'utf-8')
			if flag =='0':
				dlg = wx.MessageDialog(None, "MD5校验错误，上传失败", "警告", wx.YES_NO | wx.ICON_QUESTION)
				if dlg.ShowModal() == wx.ID_YES:
					dlg.Close(True)
				dlg.Destroy()
			else:
				dlg = wx.MessageDialog(None, "上传成功", "提醒", wx.YES_NO | wx.ICON_QUESTION)
				if dlg.ShowModal() == wx.ID_YES:
					dlg.Close(True)
			dlg.Destroy()
			sock.close()
			frame.Main.up.Destroy()



class sendM(threading.Thread):
        
	def __init__(self, *args, **kwargs):
		super(sendM, self).__init__(*args, **kwargs)
		pass
		
	def start(self ,event):
		data = frame.Main.Edit.GetValue()
		frame.Main.Edit.SetValue("")
		if data.strip() != "":  
			frame.Main.TalkList.BeginTextColour(wx.Colour(0,64,0))
			msgcontent = '我:'+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 
			frame.Main.TalkList.AddParagraph(msgcontent)
			frame.Main.TalkList.BeginTextColour(wx.Colour(0,0,0))
			jpg_data_re = re.compile('\[\d{2}\]')
			jpg_data = jpg_data_re.finditer(data)
			start_point = 0
			end_point = 0
			flag = 0
			for i in jpg_data:
				flag = flag + 1
				jpg = i.group()
				start_point = end_point
				end_point = i.start()
				frame.Main.TalkList.AddParagraph(data[start_point:end_point])
				end_point = i.end()
				jpg = data[i.start() + 1 : i.end() - 1]
				frame.Main.TalkList.AddImage(wx.Image('emoji/'+ jpg +'.jpg', wx.BITMAP_TYPE_ANY))
			if flag == 0:
				frame.Main.TalkList.AddParagraph(data)
			#frame.Main.TalkList.AddParagraph(data)
			frame.Main.TalkList.MoveDown(2)
			frame.tcpClient.sendall(data.encode(encoding='utf-8'))  # 发送数据
		else :
			dlg = wx.MessageDialog(None, "请输入相关信息", "警告", wx.YES_NO | wx.ICON_QUESTION)
			if dlg.ShowModal() == wx.ID_YES:
				dlg.Close(True)
			dlg.Destroy()


class receM(threading.Thread):

	def __init__(self, *args, **kwargs):
		super(receM, self).__init__(*args, **kwargs)
		self.__flag = threading.Event()     # 用于暂停线程的标识
		self.__flag.set()       # 设置为True
		self.__running = threading.Event()      # 用于停止线程的标识
		self.__running.set()      # 将running设置为True

	def run(self):
		while 1:
			rec_name = frame.tcpClient.recv(1024)
			rec_data = frame.tcpClient.recv(1024)  # 接收数据和返回地址
			msgcontent = rec_name.decode(encoding = 'utf-8') + ':'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			frame.Main.TalkList.BeginTextColour(wx.Colour(0, 0, 64))
			frame.Main.TalkList.AddParagraph(msgcontent)
			frame.Main.TalkList.BeginTextColour(wx.Colour(0, 0, 0))
			data = rec_data.decode(encoding='utf-8')
			jpg_data_re = re.compile('\[\d{2}\]')
			jpg_data = jpg_data_re.finditer(data)
			start_point = 0
			end_point = 0
			flag = 0
			for i in jpg_data:
				flag = flag + 1
				jpg = i.group()
				start_point = end_point
				end_point = i.start()
				#print(data[start_point:end_point])
				frame.Main.TalkList.AddParagraph(data[start_point:end_point])
				end_point = i.end()
				jpg = data[i.start() + 1 : i.end() - 1]
				frame.Main.TalkList.AddImage(wx.Image('emoji/'+ jpg +'.jpg', wx.BITMAP_TYPE_ANY))
			if flag == 0:
				frame.Main.TalkList.AddParagraph(data)
			#frame.Main.TalkList.AddParagraph(rec_data.decode(encoding='utf-8'))

	def pause(self):
		self.__flag.clear()     # 设置为False, 让线程阻塞

	def resume(self, event):
		self.__flag.set()    # 设置为True, 让线程停止阻塞
		self.__running.set()      # 将running设置为True

	def stop(self):
		self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
		self.__running.clear()        # 设置为False


class loginlist(threading.Thread):

	def __init__(self, *args, **kwargs):
		super(loginlist, self).__init__(*args, **kwargs)
		pass

	def run(self):
		Address = "119.28.133.55"
		port = 23335 #接口选择大于10000的，避免冲突
		bufsize = 1024  #定义缓冲大小
		addr = (Address,port) # 元祖形式
		while 1:
			Pl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			Pl.connect(addr)
			send_data = frame.Main.tName.encode(encoding = 'utf-8')
			#print(frame.Main.tName)
			Pl.sendall(send_data)
			try:
				rec_name = Pl.recv(bufsize)
				frame.Main.OnlinePL.Clear()
				frame.Main.OnlinePL.AppendText(rec_name.decode(encoding = 'utf-8'))

				rec_file_name = Pl.recv(bufsize)
				frame.Main.FileList.Clear()
				frame.Main.FileList.AppendText(rec_file_name.decode(encoding = 'utf-8'))

			except Exception as e:
				pass
			Pl.close()
			time.sleep(5)

class MyPanel1 ( wx.Frame ):
           
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL|wx.VSCROLL|wx.HSCROLL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		for i in range(3):
			bSizer = wx.BoxSizer( wx.HORIZONTAL )
			for k in range(4):
				index = i*4+(k+1)
				if index <10 :
					index = '0' + str(index)
				else :
					index = str(index)
				btn = wx.BitmapButton( self, wx.ID_ANY,  wx.Bitmap(wx.Image('emoji/' + index + '.jpg', wx.BITMAP_TYPE_ANY)), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
				bSizer.Add( btn, 0, wx.ALL, 5 )
				self.Bind(wx.EVT_BUTTON, lambda evt, mark = index : self.Add(evt,mark) ,btn )
			bSizer1.Add( bSizer, 1, wx.EXPAND, 5 )
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
	def __del__( self ):
		pass

	def Add(self, event, mark):
		frame.Main.Edit.AppendText("[" + mark + "]")
		frame.Main.flag = 0
		self.Destroy()

if __name__ == '__main__':
	app = wx.App(False)  
	frame = LoginLayout(None)
	frame.Show(True)    
	app.MainLoop() 
