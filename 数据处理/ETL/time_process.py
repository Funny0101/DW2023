# 从去重数据中获取release_date表所需要的字段
import pandas as pd
from datetime import datetime

# 读取CSV文件
input_file = 'data/movie_info_deduplication.csv'
output_file = 'data/date_table.csv'
df = pd.read_csv(input_file)

# 提取ASIN和Release date列
df['Release date'] = pd.to_datetime(df['Release date'], format='%d-%b-%y', errors='coerce')

# 提取年、月、日、季度、星期和周数
df['year'] = df['Release date'].dt.year
df['month'] = df['Release date'].dt.month
df['day'] = df['Release date'].dt.day
df['season'] = (df['Release date'].dt.month - 1) // 3 + 1
df['weekday'] = df['Release date'].dt.weekday + 1  # Adding 1 to start from Monday
df['week_num'] = df['Release date'].dt.isocalendar().week

# # 将缺失的日期字段填充为空字符串
# df = df.fillna(pd.NaT)

# 选择需要的列
selected_columns = ['movie_id', 'Release date','year', 'month', 'day', 'season', 'weekday', 'week_num']

# 保存结果到新的CSV文件
df[selected_columns].to_csv(output_file, index=False, float_format='%.0f')


print(f"结果已保存到 {output_file}")