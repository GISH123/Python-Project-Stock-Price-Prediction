filename = 'bda2019_hw2_table.xlsx'
import pandas as pd

print('Loading data')
keylist = pd.read_excel(filename, 'L2_foxconn_keyword')[u'term'].tolist()
content = pd.read_excel('hw1_text.xlsx',"foxconn")[u'內容'].tolist()

df_dict = dict()  #這是一個dictionary

def find_grams(article, output_list):
	"""
	輸出一個長度為245的list(此為稀疏向量)
	"""
	

	for i in range(len(keylist)):
		output_list[i] = article.count( keylist[i] )
	for i in range(len(output_list)):
		if output_list[i] >0:
			try:
				df_dict[keylist[i]] += 1
			except:
				df_dict[keylist[i]] = 1



		
# Point object define
from  math import log10, sqrt
class Point :
	def __init__(self, alist, ID='Null'):	#此alist代表1個點的座標，比如說x,y,z平面的 (-1,0,2) 這個點就是 Point( [-1, 0, 2] )
		self.list = alist
		self.given_ID = ID
		
		self.get_adjusted_list()
		self.idf_weighted_list = []
		self.cos_dict = dict()
		
	def get_adjusted_list(self):
		alist = self.list
		for i in range(len(alist)):
			if alist[i]!= 0 :
				alist[i] = 1 + log10(alist[i])
		
		lenth_of_the_vector = 0
		for value in sorted(alist, reverse = True):
			if value == 0 :
				break
			else:
				lenth_of_the_vector+= pow( value , 2 )
		lenth_of_the_vector = sqrt(lenth_of_the_vector)

		self.adjusted_list  = list(map(lambda x: x/lenth_of_the_vector, alist))
		return self.adjusted_list
		
	def get_idf_weighted_list(self, dictionary, total_number):
		alist = self.adjusted_list
		for i in range(len(alist)):
			if alist[i]!= 0 :
				df = dictionary[keylist[i]]
				alist[i] *= log10(total_number/df)
		self.idf_weighted_list = alist
		return alist

	def find_related_document(self, n):	#return 前 n 個最相近的文章
		count = 0
		return_list = []
		for value, key in sorted(zip( self.cos_dict.values(), self.cos_dict.keys() ) ,  reverse = True):
			count+=1
			if count <= n:
				return_list.append(key)
			else:
				break
		return return_list
		
Points_list = []		
id = 0
for article in content:
    id +=1
    print(id)
    output_list = [0]*245

    find_grams(article, output_list)
    Points_list.append(    Point(output_list, id)   )	

Total_number_of_documents = id
idf_weighted_list = []

print('Processing idf_weighted_list')
for point in Points_list:
	weighted_list = point.get_idf_weighted_list(df_dict, Total_number_of_documents)
	idf_weighted_list.append(	weighted_list )

	
import time
t1 = time.time()
'''舊的方法，比較慢，得花289秒
for i in range(Total_number_of_documents-1):
	for j in range(i+1, Total_number_of_documents):
		print('Processing cos_similarity', i+1, 'article v.s', j+1, 'article.')
		cos_similarity = 0
		# 看一下 i 與 j 向量誰的0的數比較少
		i_n_of_zero = idf_weighted_list[i].count(0)	#i向量中0的數量
		j_n_of_zero = idf_weighted_list[j].count(0)	#j向量中0的數量
		
		if i_n_of_zero >= j_n_of_zero:
			for value_i, value_j in sorted(zip( idf_weighted_list[i], idf_weighted_list[j]) , reverse = True):
				if value_i != 0 :
					cos_similarity += value_i * value_j
				else:
					break
					
		else:
			for value_j, value_i in sorted(zip( idf_weighted_list[j], idf_weighted_list[i]) , reverse = True):
				if value_j != 0 :
					cos_similarity += value_i * value_j
				else:
					break					
		Points_list[i].cos_dict[j+1] = cos_similarity
		Points_list[j].cos_dict[i+1] = cos_similarity
		
print('Finished! Total time consumed is', time.time()-t1, 'by using basic caculation.')	#花 289秒
'''
import numpy as np
for i in range(Total_number_of_documents-1):
	for j in range(i+1, Total_number_of_documents):
		print('Processing cos_similarity', i+1, 'article v.s', j+1, 'article.')
		cos_similarity = np.dot(	np.array(idf_weighted_list[i]), np.array(idf_weighted_list[j])	) 
						
		Points_list[i].cos_dict[j+1] = cos_similarity
		Points_list[j].cos_dict[i+1] = cos_similarity
print('Finished! Total time consumed is', time.time()-t1, 'by using np.dot.')	#花140秒 




 









### 取得對應的三篇相關文章
quary =[64, 219, 585, 1009, 164, 1657]
for i in quary:
	list1 = Points_list[i].find_related_document(3)		
	print('\n')
	print('Outputs of quary', i, 'are:')
	for j in list1:
		print('article', j-1)
		print(content[j-1])
		
		
while True:
	input_query = int( input('Type the article number, then the output will be the first most related three articles:' ) )
	list1 = Points_list[input_query-1].find_related_document(3)
	print('\n')
	print('Outputs of quary', input_query, 'are:')
	for j in list1:
		print('article', j)
		print(content[j-1])