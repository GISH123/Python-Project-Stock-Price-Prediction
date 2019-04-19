corpus_file = r'C:\Users\User\forum_ready.csv'
keys_file = r'C:\Users\User\Documents\GitHub\Big_data_analytics\mid project\data\forum cluster\1000_keywords.txt'
	


keylist = []
with open( keys_file, 'r') as file:
    for data in file.readlines():
        data = data.strip()
        keylist.append(data)
		
import pandas as pd

print('Loading data')
df = pd.read_csv(corpus_file, encoding = 'utf-8')
content = df['content'].tolist()
ids = df['id'].tolist()
del df

df_dict = dict()  #這是一個dictionary

def find_grams(article, output_list):
	"""
	輸出一個長度為1000的list(此為稀疏向量)
	"""
	

	for i in range(len(keylist)):
		if keylist[i][0] not in 'abcdefghijklmnopqrstuvwxyz':
			output_list[i] = article.count( keylist[i] )
		else:
			small_number = article.count( keylist[i] )
			
			output_list[i] = article.count( keylist[i].upper() ) + small_number
			
	for i in range(len(output_list)):
		if output_list[i] >0:
			try:
				df_dict[keylist[i]] += 1
			except:
				df_dict[keylist[i]] = 1



		
# Point object define
from  math import log10, sqrt
class Point :
	def __init__(self, alist):	#此alist代表1個點的座標，比如說x,y,z平面的 (-1,0,2) 這個點就是 Point( [-1, 0, 2] )
		self.list = alist

		if self.list.count(0) != 1000:
			self.get_adjusted_list()

		
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

		self.list  = list(map(lambda x: x/lenth_of_the_vector, alist))

		
	def get_idf_weighted_list(self, dictionary, total_number):
		if self.list.count(0) != 1000:
			alist = self.list
			for i in range(len(alist)):
				if alist[i]!= 0 :
					df = dictionary[keylist[i]]
					alist[i] *= log10(total_number/df)
			del self.list 

			return alist
		else:
			return self.list
		
Points_list = []		
id = 0
for article in content:
    id +=1
    print(id)
    output_list = [0]*len( keylist )

    find_grams(article, output_list)
    Points_list.append(    Point(output_list)   )	

del content
Total_number_of_documents = id

del id, output_list
print('Processing idf_weighted_list')

import csv #寫入檔案
file1 = 	open(r'C:\Users\User\forum_1000_tf_idf.csv' , 'w',newline='', encoding = 'utf-8')
csv_writer = csv.writer(file1)
csv_writer.writerow(['id']+keylist)



for i in range(len(Points_list)):
	print('Processing idf_weighted_list', i)
	weighted_list = Points_list[i].get_idf_weighted_list(df_dict, Total_number_of_documents)
	Points_list[i] = 0
	csv_writer.writerow( [ids[i]]+ weighted_list )
		









