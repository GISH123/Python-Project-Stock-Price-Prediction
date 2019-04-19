import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
dataset_array = pd.read_csv(r'C:\Users\User\forum_1000_tf_idf.csv').iloc[:,1:].values

print(dataset_array.shape)


import time

t1 = time.time()
kmeans = KMeans(n_init  = 4, n_jobs  =4 , n_clusters= 10 , random_state=0).fit(dataset_array)
print('花費', time.time()-t1)

import csv #寫入檔案
file1 = 	open(r'C:\Users\User\cluster.csv' , 'w',newline='', encoding = 'utf-8')
csv_writer = csv.writer(file1)
csv_writer.writerow(['cluster'])
for item in kmeans.labels_.tolist():
	csv_writer.writerow( [item] )
file1.close()

## choose the best k 

# Sum_of_squared_distances = []

# K = range(5,16)
# for k in K:
	# print('k-means with cluster =', k)
	# km =  KMeans(n_init  = 4, n_jobs  =4 , n_clusters= k, random_state=0).fit(dataset_array) 
	# Sum_of_squared_distances.append(km.inertia_)
	
# import matplotlib.pyplot as plt
# plt.plot(K, Sum_of_squared_distances, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Sum_of_squared_distances')
# plt.title('Elbow Method For Optimal k')
# plt.show()