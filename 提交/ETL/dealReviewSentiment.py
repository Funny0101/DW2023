import pandas as pd

# 假设数据文件名为 'review_sentiments.csv'
# 读取数据时只加载需要的两列，以提高效率
file_path = 'reviews_with_sentiment.csv'
df = pd.read_csv(file_path, usecols=['productId', 'sentiment_score'])

# 计算每个productId的好评（sentiment_score > 0.2）的百分比
# 首先，创建一个新的列，标记好评为1，非好评为0
df['positive_review'] = (df['sentiment_score'] >= 0.2).astype(int)

# 然后，按照productId分组，并计算好评的比例
result = df.groupby('productId')['positive_review'].mean()

# 将结果转换为DataFrame并重置索引，以便保存为CSV
result_df = result.reset_index()
result_df.columns = ['productId', 'positive_review_percentage']

# 保存结果到新的CSV文件
result_df.to_csv('product_sentiment_percentages.csv', index=False)
