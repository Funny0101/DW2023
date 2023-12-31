import glob

from textblob import TextBlob
import pandas as pd
import gc

# 第一步
# #测试用例，先抽100条
# df = pd.read_csv('f:/reviews_sorted.csv')
# first_100_rows = df.head(100)
# # 将前十行数据保存为新的 CSV 文件
# first_100_rows.to_csv('f:/first_100_rows.csv', index=False)


# 第二步
# 正式进行情感分析，每一百万条保存一次
#
# df = pd.read_csv('reviews_sorted.csv')
#
# j=0
# #定义情感分析函数
# def analyze_sentiment(text):
#     global j
#     j+=1
#     if(j%1000==0):
#         print(j)
#     analysis = TextBlob(str(text))
#     # 返回情感得分对应的评价
#     score=analysis.sentiment.polarity
#     sentiment_judge=""
#     if(-1 <= score < -0.2):
#         sentiment_judge="negative"
#     elif(-0.2 <= score <= 0.2):
#         sentiment_judge = "neutral"
#     else:
#         sentiment_judge = "positive"
#     return analysis.sentiment.polarity,sentiment_judge
#
#
# batch_size = 1000000  # 设置每批次保存的行数
# num_batches = -(-len(df) // batch_size)  # 计算总批次数
#
# for i in range(num_batches):
#     start_idx = i * batch_size
#     end_idx = min((i + 1) * batch_size, len(df))
#
#     batch_df = df.iloc[start_idx:end_idx].copy()  # 提取批次数据
#
#     # 对 'text' 列进行情感分析并保存结果到新列
#     batch_df[['sentiment_score', 'sentiment_judge']] = batch_df['text'].apply(
#         lambda text: pd.Series(analyze_sentiment(text)))
#
#     # 保存当前批次的数据到 CSV 文件
#     filename = f'reviews_with_sentiment_batch_{i}.csv'
#     batch_df.to_csv(filename, index=False)


# # 第三步
# # 输出测试，查看分析结果是否正确
# df = pd.read_csv('reviews_with_sentiment_batch_7.csv')
# # first_100_rows = df.head(50)
# # print(first_100_rows)
# negative_reviews = df[df['sentiment_judge'] == 'negative'].head(3)['text']
# pd.set_option('display.max_colwidth', None)  # 设置列宽，显示全部文本内容
# pd.set_option('display.max_rows', None)  # 设置最大行数，显示所有行
# print(negative_reviews)

# 第四步，合并csv
# 获取所有CSV文件的文件名
file_list = glob.glob('reviews_with_sentiment_batch_*.csv')
# 读取所有CSV文件并合并为一个DataFrame
all_data = pd.concat([pd.read_csv(file) for file in file_list], ignore_index=True)
# 保存合并后的DataFrame为一个新的CSV文件
all_data.to_csv('reviews_with_sentiment.csv', index=False)

