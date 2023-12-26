'''
一些零散简单函数
用作数据微调和补充
'''

import pickle
from collections import defaultdict

import pandas as pd
import re
from datetime import datetime

from fuzzywuzzy import process, fuzz


'''
合并之前爬取漏的数据
'''
def copyData():
    # 读取output.csv和movie_data_raw.csv文件
    output = pd.read_csv('./movie_info_filtered-1.csv', encoding='utf-8')

    movie_data_raw = pd.read_csv('./movie_review_num.csv', encoding='utf-8')
    # 清理'movie_data_raw' DataFrame 中的 'productId' 列的制表符
    # movie_data_raw['ASIN'] = movie_data_raw['ASIN'].str.strip('\t')
    movie_data_raw.drop_duplicates(subset=['ASIN'], keep='first', inplace=True)
    # filter_movie_data_raw = movie_data_raw[['ASIN', 'review_num']].reset_index(drop=True)

    # 使用'productId'列将两个DataFrame合并
    merged_data = pd.merge(output, movie_data_raw, on='ASIN', how='left')

    # 保存修改后的output到output.csv文件
    merged_data.to_csv('./movie_info_filtered_add_review_num.csv', index=False, encoding='utf-8')


'''
将评论最早时间用作电影上映时间（为空的时候）
'''
def addExtraTime():
    # 抽取用户评论中的最早时间作为电影上映时间
    # 读取output.csv和movie_data_raw.csv文件
    output = pd.read_csv('./output.csv', encoding='utf-8')

    review_time = pd.read_csv('./review_time.csv', encoding='utf-8')

    # 将review_time DataFrame转换为字典，以便根据productID查找reviewTime
    review_time_dict = review_time.set_index('productID')['reviewTime'].to_dict()

    # 定义一个函数，将时间戳转换为指定格式的日期
    def convert_timestamp_to_date(timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%B %d, %Y')

    # 遍历output DataFrame中的每一行，如果release_date为空，则根据productID查找reviewTime并转换为指定格式的日期
    for index, row in output.iterrows():
        if pd.isnull(row['movie_release_date']):
            product_id = row['movie_id']  # 假设'movie_id'是output DataFrame中的列名，您可以根据实际情况修改
            if product_id in review_time_dict:
                review_time = review_time_dict[product_id]
                formatted_date = convert_timestamp_to_date(review_time)
                output.at[index, 'movie_release_date'] = formatted_date

    # 将结果保存到新的CSV文件
    output.to_csv('./output_with_time.csv', index=False, encoding='utf-8')


'''
提取关键电影信息
存储到图数据库用
'''
def filterMovie():
    movies = pd.read_csv('./movie_info_filtered_add_review_num.csv', encoding='utf-8')

    # 保留指定字段
    selected_columns = ['ASIN', 'Title', 'Genres', 'review_num']

    movies = movies[selected_columns]

    movies.to_csv('./movie.csv', index=False, encoding='utf-8')


'''
建立导演和电影间的执导关系
建议演员和电影间的演出关系
存储到图数据库用
'''
def createRelation():
    actors = pd.read_csv('./actorwithid.csv', encoding='utf-8')
    directors = pd.read_csv('./directorwithid.csv', encoding='utf-8')
    movies = pd.read_csv('./movie_info_filtered-1.csv', encoding='utf-8')

    # 将 'actor_name' 列设置为索引，然后将其转换为字典
    actor_map = actors.set_index('actor_name')['actor_id'].to_dict()
    director_map = directors.set_index('director_name')['director_id'].to_dict()

    # 优化代码
    act_rows = []
    direct_rows = []

    for index, row in movies.iterrows():
        movie_id = row['ASIN']
        movie_main_actors = set(row['main_actor'].split(',')) if pd.notna(row['main_actor']) else set()

        if pd.notna(row['Actors']):
            movie_actors = [actor.strip() for actor in row['Actors'].split(',')]
            for actor_name in movie_actors:
                if actor_name in actor_map:
                    actor_id = actor_map[actor_name]
                    is_main_director = actor_name in movie_main_actors
                    act_rows.append({'actor_id': actor_id, 'movie_id': movie_id, 'is_main_actor': is_main_director})

        if pd.notna(row['Directors']):
            movie_directors = [director.strip() for director in row['Directors'].split(',')]
            for director_name in movie_directors:
                if director_name in director_map:
                    director_id = director_map[director_name]
                    direct_rows.append({'director_id': director_id, 'movie_id': movie_id})

    # 使用pd.concat将列表中的行连接到DataFrame
    act = pd.DataFrame(act_rows)
    direct = pd.DataFrame(direct_rows)

    act.drop_duplicates(subset=['actor_id', 'movie_id'], keep='first', inplace=True)
    direct.drop_duplicates(subset=['director_id', 'movie_id'], keep='first', inplace=True)

    # 将结果保存到新的CSV文件
    direct.to_csv('./direct.csv', index=False, encoding='utf-8')
    act.to_csv('./act.csv', index=False, encoding='utf-8')


'''
抽取出导演和演员信息
存储到图数据库用
'''
def getNames():
    raw_data = pd.read_csv('./movie_info_filtered-1.csv', encoding='utf-8')

    # 首先将所有姓名全都抽取出来
    director_name_set = set()
    actor_name_set = set()

    for index, row in raw_data.iterrows():
        # director
        director_names = row['Directors']
        if isinstance(director_names, str):
            for director_name in director_names.split(','):
                director_name_set.add(director_name.strip())  # 使用strip()函数去除名字前后的空格
        # starring
        starring_names = row['main_actor']
        if isinstance(starring_names, str):
            for starring_name in starring_names.split(','):
                actor_name_set.add(starring_name.strip())
        # actor
        actor_names = row['Actors']
        if isinstance(actor_names, str):
            for actor_name in actor_names.split(','):
                actor_name_set.add(actor_name.strip())

    # 假设 name_set 是一个集合，你可以使用下面的示例代码创建一个 DataFrame
    director_name_df = pd.DataFrame(list(director_name_set), columns=['director_name'])
    actor_name_df = pd.DataFrame(list(actor_name_set), columns=['actor_name'])
    # 将 DataFrame 保存为 CSV 文件
    director_name_df.to_csv('./director_names.csv', index=False, encoding='utf-8')
    actor_name_df.to_csv('./actor_names.csv', index=False, encoding='utf-8')


'''
建立电影和和替换电影的ID映射关系
'''
def mapID():
    output = pd.read_csv('./new_movies_info_整理title.csv', encoding='utf-8')

    # 处理空值，将movie_director和movie_title列的空值替换为空字符串
    output['Directors'] = output['Directors'].fillna('')
    output['Title'] = output['Title'].fillna('')

    # 将 movie_title 和 movie_director 合并成一个新的列，以便后续的 groupby 操作
    output['title_director'] = output['Title'].str.lower() + '_' + output['Directors'].str.lower()

    # 使用 groupby 和 transform 获取每个重复组的第一次出现的 id
    output['first_occurrence_id'] = output.groupby('title_director')['ASIN'].transform('first')

    # 创建一个哈希表，用于存储重复项和对应的第一项的id的映射
    id_mappings = {}

    # 遍历 DataFrame 的每一行
    for _, row in output.iterrows():
        current_id = row['ASIN']
        first_occurrence_id = row['first_occurrence_id']

        if pd.notna(first_occurrence_id) and current_id != first_occurrence_id:
            id_mappings[current_id] = first_occurrence_id

    # print(id_mappings)
    # 存储映射表到二进制文件
    with open('id_mappings.pkl', 'wb') as file:
        pickle.dump(id_mappings, file)