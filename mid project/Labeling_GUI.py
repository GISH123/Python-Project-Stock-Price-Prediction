'''
注意

必須要更改兩個地方才能使用此程式

1.讀檔的地方
2.儲存檔案的地方

讀檔的檔案地址: 如果有下載我清洗過的檔案請輸入 news_ready.csv，否則輸入老師給的 news.csv

第一頁 輸入 兩個數字，代表要標記的範圍 e.g. 輸入10 跟 20 代表要標記 id = 10~20 共11篇

也請注意編碼問題，我的檔案編碼為big5
'''

# file_in = r'C:\Users\User\Desktop\大數據與商業分析\mid tern\news.csv'
file_in = r'C:\Users\User\news_ready.csv'


#存檔的目標"資料夾"地址:	e.g r'‪C:\Users\User\Desktop'
file_out = r'C:\Users\User'

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import *
import pandas as pd
import re, csv
import time

df = pd.read_csv(file_in, encoding = 'big5')
start = 0
end = 1
count = -1
Frame_dict = {}
label_dict = {}


class TwoPageApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		
		frame = self.frames[cont]
		frame.tkraise()
		global Frame_dict
		Frame_dict = self.frames

class StartPage(tk.Frame):


	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		
		f = tkFont.Font(size = 18, family = "Courier New")

		self.lblNum1 = tk.Label(self, text = u"請輸入你想要標記的區間，只能有數字", height = 5, width = 100, font = f,fg = "white", bg = "red")
		self.lblNum2 = tk.Label(self, text = u"開始", height = 5, width = 15, font = f,fg = "white", bg = "red")
		self.lblNum3 = tk.Label(self, text = u"結束", height = 5, width = 15, font = f,fg = "white", bg = "red")



		self.btnNext = tk.Button(self, text="下一頁", height = 5, width = 18,font = f, fg = "white", bg = "black",
					command = lambda: controller.show_frame(PageOne))##
					
		self.btngetvalues = tk.Button(self, text="輸入完畢", height = 5, width = 18,font = f, fg = "white", bg = "black",
					command = self.getvalues )##			
					
		self.lblNum1.grid(row = 0, column = 0 ,sticky = "NEWS", columnspan = 2)
		self.lblNum2.grid(row = 1, column = 0 ,sticky = "NEWS")
		self.lblNum3.grid(row = 2, column = 0 ,sticky = "NEWS")

		self.btnNext.grid(row = 4, column = 0,  sticky = "NEWS", columnspan = 2)			
		self.btngetvalues.grid(row = 3, column = 0,  sticky = "NEWS", columnspan = 2)

################################################# self.enterNums
		self.enterNums = []
		for i in range(2):
			self.enterNums.append(tk.Entry(self, width = 5, font = f))
			self.enterNums[i].grid(row = i+1, column = 1, sticky = "NEWS")


	def getvalues(self):
		global start, end, title, content, label_dict, ids
		list = []
		for i in self.enterNums:
			list.append( i.get() )
		
		
		try:
			start, end = int(list[0]), int(list[1])
			#把title以及content提取出來
			title = df[start:end+1]['title'].tolist()
			content = df[start:end+1]['content'].tolist()
			content = [re.sub('<BR>', '', i) for i in content]
			ids = df[start:end+1]['id'].tolist()
			
			#更新第一欄標示
			if end >start :
				self.lblNum1.config(text = '你選取的區間為:%i~%i，共%i篇' %(start, end, end-start+1))
				self.btngetvalues.config(	text = '點擊下一頁以繼續，你也可以重新輸入後再點我一次。')
			else:
				self.lblNum1.config(text = '你輸入區間不合乎規定，必須為兩個整數，並第二個數字需比較大。')
				self.btngetvalues.config(text = '輸入完畢')
		except:
			self.lblNum1.config(text = '你輸入區間不合乎規定，必須為兩個整數，並第二個數字需比較大。')
			self.btngetvalues.config(text = '輸入完畢')
			
class PageOne(tk.Frame):
	
	def __init__(self, parent, controller):
		'''
		基本東西，初始介面
		'''

		self.count = -1

		f = tkFont.Font(size = 12, family = "Courier New")
		
		tk.Frame.__init__(self, parent)			

		#標註
		self.lbl1 = tk.Label(self, text = u"即將標記文章" , height = 1, width = 90, font = f,fg = "white", bg = "red")
		self.lbl1.grid(row = 0, column = 0 ,sticky = "NEWS")
		self.lbl2 = tk.Label(self, text = u"按上一頁能回到前頁，如果你曾標過這篇，將會幫你選取。標記一篇後會自動跳到下一頁，你也可以按下一頁來換頁。" , height = 1, width = 90, font = f,fg = "white", bg = "red")
		self.lbl2.grid(row = 1, column = 0 ,sticky = "NEWS")		

		self.lbl3 = tk.Label(self, text = u"系統會自動存檔，每5篇，或者全部標完後會存在你指定的資料夾。" , height = 1, width = 90, font = f,fg = "white", bg = "red")
		self.lbl3.grid(row = 2, column = 0 ,sticky = "NEWS")

		
		#下一頁
		self.btnNext = tk.Button(self, text="下一頁", height = 1, width = 8,font = f, fg = "white", bg = "black",	command = lambda: self.update_frame() )##
		self.btnNext.grid(row = 8, column = 0,  sticky = "NEWS")	

	def label_change(self):
		'''
		標記文章的改變，將會改變label_dict這個字典
		'''
		global label_dict
		self.label = self.var1.get()
		label_dict[  ids[self.count] ] = self.label
		print(label_dict)
		
		#自動存檔功能
		if len(label_dict) % 10 == 0 or len(label_dict) == self.target_length:
			self.save_file()
		if self.count  < self.target_length - 1:	
			self.update_frame()
		elif len(label_dict) == self.target_length:
			self.lblCount.config(text = '全部標記，恭喜!')
	
	def save_file(self):
		'''
		當按下離開之後，將會存檔，存成csv檔案
		'''
		global label_dict, ids, start, end
		write_f = open( file_out + r'\labeled_%i_%i.csv' %(start, end),  'w', newline='')
		csv_writer = csv.writer(write_f)
		csv_writer.writerow(['id','label'])
		for id in ids:
			try:
				csv_writer.writerow([id , label_dict[id]])
			except:
				pass
	
	def donothing(self):
		'''
		啥事也不做，為了頁初跟頁尾
		'''
		pass
		
	def prev_frame(self):	
		'''
		每當pageone按下 '上一頁' 按鈕後，將會更新介面，以下是新介面的設定
		'''	
		self.count -= 2
		self.update_frame()
		
	def update_frame(self):
		'''
		每當pageone按下 '下一頁' 按鈕後，將會更新介面，以下是新介面的設定
		'''		
		global label_dict, start,end

		
		#font and attribue
		f = tkFont.Font(size = 10, family = "Courier New")
		self.count+=1
		f_content = tkFont.Font(size = 12, family = "Courier New")
		self.target_length = end-start + 1
		self.var1 = tk.StringVar()
		

		
		
		#widget and grid
		
		#Counter
		self.lblCount = tk.Label(self, text = u"你已經完成了%i / %i篇標記。" % ( len(label_dict), self.target_length ), height = 1, width = 15, font = f,fg = "white", bg = "red")
		self.lblCount.grid(row = 0, column = 0 ,sticky = "NEWS",columnspan = 5)			
		
		#Title
		self.lblTitle = tk.Label(self, text = u'標題: \n%s' % title[self.count], height = 2, width = 15, font = f,fg = "white", bg = "blue")
		self.lblTitle.grid(row = 1, column = 0 ,sticky = "NEWS",columnspan = 5)			
		
		#Content
		self.lblContent = tk.Label(self, text = u'本文: \n%s' % content[self.count], height = 30, width = 135, font = f_content,fg = "white", bg = "black",
wraplength =1300,
justify = 'left')
		self.lblContent.grid(row = 2, column = 0 ,sticky = "NEWS",columnspan =5)		

		#Check_button
		

			
		
		self.Checkbutton_up =  tk.Radiobutton(self, text=u'看漲文章',  indicatoron=0, bd=14, variable=self.var1, value = 'up', command= self.label_change )
		self.Checkbutton_flat =  tk.Radiobutton(self, text=u'不相關文章', indicatoron=0, bd=14,  variable=self.var1, value = 'flat', command= self.label_change )
		self.Checkbutton_down =  tk.Radiobutton(self, text=u'看跌文章', indicatoron=0, bd=14, variable=self.var1, value = 'down',	command= self.label_change )
		self.Checkbutton_up.grid(row = 7, column = 0 ,sticky = "NEWS",columnspan = 1)	
		self.Checkbutton_down.grid(row = 7, column = 1 ,sticky = "NEWS",columnspan = 1)
		self.Checkbutton_flat.grid(row = 7, column = 2 ,sticky = "NEWS",columnspan = 1)	
		# set the default value
		if ids[self.count] in label_dict:		
			labeled = label_dict[ids[self.count]]
			if labeled == 'up':
				self.Checkbutton_up.select()
			elif labeled == 'flat':
				self.Checkbutton_flat.select()
			else:
				self.Checkbutton_down.select()
		
		# Previous page button
		if self.count > 0 :
			self.btnPrev = tk.Button(self, text="上一頁", height = 1, width = 8,font = f, fg = "white", bg = "black", command = lambda: self.prev_frame() )##
			self.btnPrev.grid(row = 8, column = 0,  sticky = "NEWS")
		elif self.count==0 and len(label_dict)==0:
			self.btnPrev = tk.Button(self, text="頁初", height = 1, width = 8,font = f, fg = "white", bg = "black")
			self.btnPrev.grid(row = 8, column = 0,  sticky = "NEWS")
		else:
			self.btnPrev.config(text = '頁初', command = lambda: self.donothing() )##
			
		#Next page button
		if self.count < self.target_length - 1:
			
			self.btnNext = tk.Button(self, text="下一頁", height = 1, width = 8,font = f, fg = "white", bg = "black", command = lambda: self.update_frame() )##
			self.btnNext.grid(row = 8, column = 1,  sticky = "NEWS",columnspan = 3)
		else:
			self.btnNext.config(text = '你已經到達頁底', command = lambda: self.donothing() )##
			
		#Save button
		self.btnSave = tk.Button(self, text="存檔", height = 1, width = 8,font = f, fg = "white", bg = "black", command = lambda: self.save_file() )##
		self.btnSave.grid(row = 8, column = 4,  sticky = "NEWS", columnspan = 2 )		

		
app = TwoPageApp()
app.mainloop()
