# 公告
這堂課是大數據與商業分析 2019 Spring\
我將紀錄課堂所學

# 課堂內進度
## hw1
* Text mining: 使用2-6 gram技術來採取關鍵字

## hw2
給定關於鴻海的語料集，使用文章向量技術，以cos_similarity當作判斷距離標準
輸入一篇文章，即可返回三篇最相近的文章

## mid project
給定2016~2018年所有台股股價資料以及這段期間的新聞、論壇、BBS文章
建構出一個以消息面(或情緒面)建構出的股價預測漲跌模型

### 台股指數漲跌
* 預測下跌準確率:77.78%, 預測上漲準確率:70.59%, 出手率:三成
* [程式碼](https://github.com/ga877439/Big_data_analytics/blob/master/mid%20project/ipy/%E7%A8%8B%E5%BC%8F%E7%A2%BC%E7%B5%B1%E6%95)

### 事件預測(台灣50成分股)
* 出手率非常低，但預測下跌準確率:63.16%
* [程式碼](https://github.com/ga877439/Big_data_analytics/blob/master/mid%20project/ipy/event_detection.ipynb)
