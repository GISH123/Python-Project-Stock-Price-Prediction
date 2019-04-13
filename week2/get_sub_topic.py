from tf_idf import contains_keyword
import pandas as pd
import csv
subtopic = [['銀行', '金融', '借貸', '網銀', '核貸', '呆帳', '轉帳', '定存', '活存' ], 
			['信用卡', '卡債', '借貸卡', '到期', '現金回饋', '信用卡帳單', '卡奴', '盜刷', '刷卡' ], 
			['匯率', '匯市','匯兌', '人民幣', '美金', '美元', '美圓', '日圓', '日元', '新台幣'],
			['台積電', '半導體', '張忠謀', '蘋果代工','晶圓', '晶圓代工', '奈米製程'], 
			['台灣', '臺灣', '全台', '全臺', '台北', '臺北', '中華台北', '中華臺北'],
			['日本', '東京', '大阪', '北海道', '日圓', '日元', '日經', '首相', '大臣']
			]
			
			
path1 = path1 = r'C:\Users\User\Desktop\大數據與商業分析\bda2019_hw1\hw1_text.xlsx'		#path need to be modified
content = pd.read_excel(path1,"all")[u'內容'].tolist()	#一個list，每個元素為文章內文

filehandler_list = []
csv_writer_list = []	#用來記錄所有的csv_writer

for i in range(6):	#創造一共六個csv_writer
	filehandler_list.append( open( r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\week2\csv_output%d.csv' %i, 'w', newline = '', encoding = 'utf-8') )
	csv_writer_list.append( csv.writer(filehandler_list[i]) )
	csv_writer_list[i].writerow([u'內容'])
	
	
	
count = 0
for article in content:
	count += 1
	print(count)
	for i in range(6):
		
		if contains_keyword(article, subtopic[i]):
			csv_writer_list[i].writerow([u'%s' % article])
			
for i in range(6):	#關掉一共六個csv_writer
	filehandler_list[i].close()