import wx
import wx.xrc
from cryptography.fernet import Fernet


class MainMenu ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PYTHON", pos = wx.DefaultPosition, size = wx.Size( 254,113 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Створити тест", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Пройти тест", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.m_button3.Bind( wx.EVT_BUTTON, self.onCreateTest )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onPassTest )
		self.Bind( wx.EVT_CLOSE,  self.onClose)
	
	def __del__( self ):
		pass
	
	def onCreateTest( self, event ):
		frame1.Hide()
		frame2.Show()

	def onPassTest (self, event ):
		frame1.Hide()
		frame3.PrepareToTest()
		frame3.Show()

	def onClose(self, event):
		wx.Exit()



class CreateQuizGeneral ( wx.Frame ):
	
	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,266 ), style = wx.CAPTION | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.questionsNumber = 10
		self.questionsDatabase = {}

		self.name = ""
		self.topic = ""

		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Назва тесту:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"Введіть назву", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Тема:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"Введіть тему", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Кількість питань:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 10, 1, 20, wx.DefaultPosition, wx.Size( 200,40 ), wx.SL_HORIZONTAL | wx.SL_LABELS)
		bSizer3.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Зберегти", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALIGN_BOTTOM|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_button4.Bind( wx.EVT_BUTTON, self.onSave )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Скасувати", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button5, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.m_button5.Bind( wx.EVT_BUTTON, self.onCancel )
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__(self):
		pass

	def onCancel(self, e):
		dlg = wx.MessageBox("Ви точно хочете скасувати створення тесту?", "Увага", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING, self)

		if dlg == wx.YES:
			frame1.Show()
			frame2.Hide()
			self.m_textCtrl1.SetValue(u"Введіть назву")
			self.m_textCtrl2.SetValue(u"Введіть тему")
			self.m_slider1.SetValue(10)

	def onSave(self, e):
		self.questionsNumber = self.m_slider1.GetValue()
		self.name = self.m_textCtrl1.GetValue()
		self.topic = self.m_textCtrl2.GetValue()
		frame2.Hide()
		frame3.Show()
		self.m_textCtrl1.SetValue(u"Введіть назву")
		self.m_textCtrl2.SetValue(u"Введіть тему")
		self.m_slider1.SetValue(10)
		frame3.m_staticText4.SetLabel(u"Питання №1")
		frame3.m_button9.Show()
		frame3.m_button10.Show()
		frame3.m_button10.GetParent().Layout()
		frame3.m_button8.GetParent().Layout()
		frame3.m_button9.GetParent().Layout()

		if self.questionsNumber == 1:
			frame3.m_button9.SetLabel("Завершити")



class QuestionCreateDefaultBlank ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,190 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.currentQuestionIndex = 1
		self.mode = 'c'
		self.points = 0

		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Питання №", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.onTextChange)
		bSizer5.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Відповідь:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.Bind( wx.EVT_TEXT, self.onTextChange)
		bSizer5.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Назад", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.Hide()
		self.m_button8.Bind( wx.EVT_BUTTON, self.onPrev )
		
		bSizer7.Add( self.m_button8, 0, wx.ALL, 5 )
		
		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Зберегти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.Hide()
		self.m_button10.Bind( wx.EVT_BUTTON, self.onSave )

		bSizer10.Add( self.m_button10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Далі", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.Hide()
		self.m_button9.Bind( wx.EVT_BUTTON, self.onNext )
		
		bSizer9.Add( self.m_button9, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def encrypt( self, path, path_f ):
		key = Fernet.generate_key()
		with open(path_f + '\\filekey.key', 'wb') as filekey: 
			filekey.write(key)
		fernet = Fernet(key)
		with open(path, 'rb') as file: 
			org = file.read() 
		
		encrypted = fernet.encrypt(org)
		with open(path, 'wb') as encrypted_file: 
			encrypted_file.write(encrypted) 

	def saveTestFile(self):
		with wx.FileDialog(self, "Save test file", wildcard="TEST files (*.test)|*.test",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			path = fileDialog.GetPath()
			path_f = fileDialog.GetDirectory()
			print(path_f)
			f = open(path, "w+")
			f.write(frame2.name+'\n')
			f.write(frame2.topic+'\n')
			f.write(str(frame2.questionsNumber)+'\n')
			for i in range (1, frame2.questionsNumber+1):
				f.write(frame2.questionsDatabase[i][0]+'\n')
				f.write(frame2.questionsDatabase[i][1]+'\n')
			f.close()
			self.encrypt(path, path_f)

	def onNext( self, event ):
		
		if self.currentQuestionIndex == frame2.questionsNumber:
			if self.mode == 'c':
				self.saveTestFile()
				wx.Exit()
			else:
				print(frame2.questionsDatabase, self.answers)
				for i in range(1, frame2.questionsNumber+1):
					
					if (frame2.questionsDatabase[i][1] == self.answers[i]+'\n'):
						self.points += 1
				wx.MessageBox("Кількість балів: " +  str(self.points), 'Тестування', wx.OK | wx.ICON_INFORMATION)
				wx.Exit()


		if (self.mode == 'c'):
			if self.currentQuestionIndex + 1 in frame2.questionsDatabase:
				self.m_button10.Disable()
			else:
				self.m_button10.Enable()
		else:
			if self.currentQuestionIndex + 1 in self.answers:
				self.m_button10.Disable()
			else:
				self.m_button10.Enable()

		if (self.mode != 'c'):
			self.m_textCtrl3.SetValue(frame2.questionsDatabase[self.currentQuestionIndex+1][0][:-1])

		if self.currentQuestionIndex == 1:
			self.m_button8.Show()
			self.m_button8.GetParent().Layout()

		self.currentQuestionIndex += 1
		self.m_staticText4.SetLabel(u"Питання №" + str(self.currentQuestionIndex))
		if self.currentQuestionIndex == frame2.questionsNumber:
			self.m_button9.SetLabel("Завершити")

	def onPrev( self, event ):
		if (self.mode == 'c'):
			if self.currentQuestionIndex - 1 in frame2.questionsDatabase:
				self.m_button10.Disable()
			else:
				self.m_button10.Enable()
		else:
			if self.currentQuestionIndex - 1 in self.answers:
				self.m_button10.Disable()
			else:
				self.m_button10.Enable()
		
		if (self.mode != 'c'):
			self.m_textCtrl3.SetValue(frame2.questionsDatabase[self.currentQuestionIndex-1][0][:-1])

		if self.currentQuestionIndex == frame2.questionsNumber:
			self.m_button9.SetLabel("Далі")

		self.currentQuestionIndex -= 1
		self.m_staticText4.SetLabel(u"Питання №" + str(self.currentQuestionIndex))
		if self.currentQuestionIndex == 1:
			self.m_button8.Hide()

	def onSave( self, event ):
		if (self.mode == 'c'):
			buf = []
			buf.append(self.m_textCtrl3.GetValue())
			buf.append(self.m_textCtrl4.GetValue())
			frame2.questionsDatabase[self.currentQuestionIndex] = buf
			self.m_button10.Disable()
			print(frame2.questionsDatabase)
		else:
			self.answers[self.currentQuestionIndex] = self.m_textCtrl4.GetValue()
			self.m_button10.Disable()
			print(self.answers)
				

	def onTextChange( self, event ):
		if not self.m_button10.IsEnabled():
			self.m_button10.Enable()

	def PrepareToTest( self ):
		fileDialog1 = wx.FileDialog(self, "Open test file", wildcard="TEST files (*.test)|*.test", style=wx.FD_OPEN)
		fileDialog2 = wx.FileDialog(self, "Open key file", wildcard="KEY files (*.key)|*.key", style=wx.FD_OPEN)
		if fileDialog1.ShowModal() == wx.ID_CANCEL:
			return
		if fileDialog2.ShowModal() == wx.ID_CANCEL:
			return
		path1 = fileDialog1.GetPath()
		path2 = fileDialog2.GetPath()

		with open(path2, 'rb') as filekey: 
			key = filekey.read() 

		fernet = Fernet(key) 

		with open(path1, 'rb') as enc_file: 
			encrypted = enc_file.read() 
  
		decrypted = fernet.decrypt(encrypted) 

		with open(path1, 'wb') as dec_file: 
			dec_file.write(decrypted)
		
		frame2.questionsDatabase = {}

		with open(path1, 'r') as f:
			frame2.name = f.readline()
			frame2.topic = f.readline()
			frame2.questionsNumber = int(f.readline())

			for i in range(1, frame2.questionsNumber+1):
				a1 = f.readline()
				a2 = f.readline()
				buf = []
				buf.append(a1)
				buf.append(a2)
				frame2.questionsDatabase[i] = buf

		self.m_textCtrl3.Disable()
		self.m_textCtrl3.SetValue(frame2.questionsDatabase[1][0][:-1])
		self.m_textCtrl4.SetValue('')
		self.currentQuestionIndex = 1
		self.mode = 'p'
		self.answers = {}
		if (frame2.questionsNumber == 1):
			self.m_button9.SetLabel("Завершити")
		self.m_button10.Show()
		self.m_button9.Show()

		self.m_staticText4.SetLabel(u"Питання №" + str(self.currentQuestionIndex))
		wx.MessageBox("Назва: " + frame2.name + "\n" + "Тема: " + frame2.topic + '\n' + "Кількість питань: " +  str(frame2.questionsNumber), 'Тестування', wx.OK | wx.ICON_INFORMATION)
		

	def __del__( self ):
		pass



app = wx.App()
frame1 = MainMenu(None)
frame2 = CreateQuizGeneral(None)
frame3 = QuestionCreateDefaultBlank(None)

frame1.Show()
app.MainLoop()
