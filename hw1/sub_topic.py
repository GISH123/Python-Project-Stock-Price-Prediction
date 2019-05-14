from tf_idf import *
import pandas as pd
import csv


import time

t1 = time.time()
path = r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\week2\csv_output5.csv'
main( path )
print('time spent is:', time.time()-t1 ) 


import csv #寫入檔案
with open(r'C:\Users\User\Documents\GitHub\Big-Data-and-Business-Analytics\week2\data\finished_output5.csv', 'w',newline='', encoding = 'utf-8-sig') as file1:
	csv_writer = csv.writer(file1)
	csv_writer.writerow(['單詞', 'TF', 'DF'])
	for n in range(2,7):
		for value,key in sorted(zip(dict_of_tf_dict[n].values(), dict_of_tf_dict[n].keys()), reverse=True):
			csv_writer.writerow([ key, value, dict_of_df_dict[n][key] ])
			
			
			
			
			
			