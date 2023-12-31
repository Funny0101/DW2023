import pandas as pd

# 读取CSV文件
movie_df = pd.read_csv('f:/movies.csv')

#筛选所有可能为电影的数据
asin_df = pd.read_csv('movie_id_save_from_review.csv')
# 获取ASIN表中的所有ASIN值
asin_values = asin_df['productId'].tolist()
print("开始过滤")
# 在movie表中过滤掉存在于ASIN表中的行
filtered_movie_df = movie_df[movie_df['ASIN'].isin(asin_values)]
print(len(filtered_movie_df))
# 将筛选后的数据保存到CSV文件中
filtered_movie_df.to_csv('possible_movie.csv', index=False)



# 读取CSV文件
movie_df = pd.read_csv('possible_movie.csv')

#筛选所有可能为TV的数据
asin_df = pd.read_csv('movie_id_from_movie.csv')
# 获取ASIN表中的所有ASIN值
asin_values = asin_df['productId'].tolist()
print("开始过滤")
# 在movie表中过滤掉存在于ASIN表中的行
filtered_movie_df = movie_df[~movie_df['ASIN'].isin(asin_values)]
print(len(filtered_movie_df))
# 将筛选后的数据保存到CSV文件中
filtered_movie_df.to_csv('filtered_movie.csv', index=False)