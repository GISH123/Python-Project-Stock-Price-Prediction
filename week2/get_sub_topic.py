
import pandas as pd
import csv

def contains_keyword(document, keyword_list):	#目前沒用到
	'''
	確認是否一個document內是否有包含keyword
	'''
	for keyword in keyword_list:
		if keyword in document:
			return True	#如果有包含 回傳True
			
	return False		#否則的話，都回傳False
	

subtopic = [["1101", "台泥"], ["1102", "亞泥"], ["1216", "統一"], ["1301", "台塑"], ["1303", "南亞"], ["1326", "台化"], ["1402", "遠東新"], ["1722", "台肥"], ["2002", "中鋼"], ["2105", "正新"], ["2207", "和泰車"], ["2227", "裕日車"], ["2301", "光寶科"], ["2303", "聯電"], ["2308", "台達電"], ["2311", "日月光"], ["2317", "鴻海"], ["2324", "仁寶"], ["2325", "矽品"], ["2330", "台積電"], ["2347", "聯強"], ["2353", "宏碁"], ["2354", "鴻準"], ["2357", "華碩"], ["2382", "廣達"], ["2409", "友達"], ["2412", "中華電"], ["2454", "聯發科"], ["2474", "可成"], ["2498", "宏達電"], ["2801", "彰銀"], ["2880", "華南金"], ["2881", "富邦金"], ["2882", "國泰金"], ["2883", "開發金"], ["2885", "元大金"], ["2886", "兆豐金"], ["2890", "永豐金"], ["2891", "中信金"], ["2892", "第一金"], ["2912", "統一超"], ["3008", "大立光"], ["3045", "台灣大"], ["3231", "緯創"], ["3481", "群創"], ["3673", "TPK-KY"], ["3697", "晨星-KY"], ["4904", "遠傳"], ["5880", "合庫金"], ["6505", "台塑化"]]
			
			
path1 = path1 = r'C:\Users\User\news_ready.csv'		#path need to be modified
df = pd.read_csv(path1, encoding = 'big5')
content = df['content'].tolist()	
title = df['title'].tolist()	
ids =  df['id'].tolist()	
time = df['post_time'].tolist()	
labels  = df['label'].tolist()	
del df

filehandler_list = []
csv_writer_list = []	#用來記錄所有的csv_writer

for i in range(len(subtopic)):	#創造一共六個csv_writer
	filehandler_list.append( open( r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\csv_output_%s.csv' %subtopic[i][0], 'w', newline = '', encoding = 'big5') )
	csv_writer_list.append( csv.writer(filehandler_list[i]) )
	csv_writer_list[i].writerow(['id', 'post_time', 'title', 'content', 'label'])
	
	
	
count = 0
for index in range(len(content)):
	article = title[index] + ' ' + content[index]
	count += 1

	print(count)
	for i in range(1, len(subtopic)):
		
		if contains_keyword(article, subtopic[i]):
			csv_writer_list[i].writerow([ u'%s' % ids[index]  , u'%s' % time[index],  u'%s' % title[index]  , u'%s' % content[index], u'%s' % labels[index]])
			
for i in range(len(subtopic)):	#關掉一共六個csv_writer
	filehandler_list[i].close()