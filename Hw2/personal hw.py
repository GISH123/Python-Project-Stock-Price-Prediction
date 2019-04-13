filename = r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\Hw2\bda2019_hw2_table.xlsx'
import pandas as pd

print('Loading data')
keylist = pd.read_excel(filename, 'L2_foxconn_keyword')[u'term'].tolist()
content = pd.read_excel(r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\Hw2\hw1_text.xlsx',"foxconn")[u'內容'].tolist()

df_list = []

#首先我們需要自己的發生機率	f(x) 或 f(y)，以及共同發生f(x,y)。
#f(x) = cnt_x / N
#f(y) = cnt_y / N
#f(x,y) = cnt_x_and_y / N

self_occur_f_list = [0] * len(keylist)
co_ocuur = [0] * len(keylist)
N_list = [0] * len(keylist)


count = 0
for article in content:
	count+=1
	print(count)
	#先找出是否該 content 有 鴻海
	
	
	
	
	for index in range(len(keylist)):
		word = keylist[index]
		
		
		#計算自己的frequency
		if word in article:
			self_occur_f_list[index] += 1
			
		#計算自己或者鴻海的所有文章	
			N_list[index] += 1	
		elif '鴻海' in article:
			N_list[index] += 1
			
		#計算共同出現的frequncy	
		if word in article and word !='鴻海' and '鴻海' in article:
			co_ocuur[index] += 1
			
# print(self_occur_f_list)
# print(co_ocuur)



support_list = [0] * len(keylist)
confidence_list =[0] * len(keylist)
lift_list = [0] * len(keylist)

##計算相關程度

fox_id  = keylist.index('鴻海')

f_x = self_occur_f_list[fox_id]

for index in range(len(keylist)):
	if index != fox_id:
		N = N_list[index]
		p_x = f_x/ N
		p_y = 	self_occur_f_list[index] / N
		p_x_and_y = co_ocuur[index] / N
		
		#計算指標
		confidence = p_x_and_y / p_x
		support = p_x_and_y
		lift = confidence / p_y
		
		confidence_list[index] = confidence
		support_list[index] = support
		lift_list[index] = lift
		
# lift_list.sort(reverse = True)		
# confidence_list.sort(reverse = True)	
# support_list.sort(reverse = False)	
# print(lift_list[:5])
# print(confidence_list[:5])
# print(support_list[:5])
		
wanted_word = []
dropped_word = []
for confidence_value, lift_value, support_value, index in sorted( zip(confidence_list, lift_list,support_list, range(len(keylist)) ), reverse = True):
	if len(wanted_word) == 20:
		break
	
	
	
	if support_value > 0.001 and lift_value > 0.9:	
		print(keylist[index], 'confidence = %.2f, support = %.2f, lift = %.2f.'	%(confidence_value, support_value, lift_value))
		wanted_word.append(keylist[index])
	else:
		dropped_word.append( (keylist[index], 'confidence = %.2f, support = %.2f, lift = %.2f.'	%(confidence_value, support_value, lift_value)) )
		
print(len(	wanted_word), wanted_word)	
		
		
for word in wanted_word:
	print(word, end = '、')






