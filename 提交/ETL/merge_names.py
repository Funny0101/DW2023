'''
合并姓名信息，包括主演、演员、导演
比如简写、小错之类的
'''

import pickle
from collections import defaultdict

import pandas as pd
import re
from datetime import datetime

from fuzzywuzzy import process, fuzz


'''
去除姓名中多余的引号，避免干扰
'''
def removeRedundantMarks():
    raw_data = pd.read_csv('./output_with_time.csv', encoding='utf-8')
    for column in ['movie_director', 'movie_starring', 'movie_actor']:
        # 遍历指定列，替换所有字符串中的多余双引号
        raw_data[column] = raw_data[column].str.replace('"', '')

    # 将处理后的数据保存到新文件
    raw_data.to_csv('./output_cleaned.csv', index=False, encoding='utf-8')


'''
csv中所有姓名提取到set中
存储到二进制文件便于下次读取
'''
def beforeMerge():
    raw_data = pd.read_csv('./output_with_time.csv', encoding='utf-8')

    # 首先将所有姓名全都抽取出来
    name_set = set()

    for index, row in raw_data.iterrows():
        # director
        director_names = row['movie_director']
        if isinstance(director_names, str):
            for director_name in director_names.split(','):
                name_set.add(director_name.strip())  # 使用strip()函数去除名字前后的空格
        # starring
        starring_names = row['movie_starring']
        if isinstance(starring_names, str):
            for starring_name in starring_names.split(','):
                name_set.add(starring_name.strip())
        # actor
        actor_names = row['movie_actor']
        if isinstance(actor_names, str):
            for actor_name in actor_names.split(','):
                name_set.add(actor_name.strip())

    # 将set保存到文件
    with open('set.pkl', 'wb') as set_file:
        pickle.dump(name_set, set_file)

    # 存储名字的映射关系
    name_mappings = defaultdict(str)
    with open('map.pkl', 'wb') as map_file:
        pickle.dump(name_mappings, map_file)


'''
首先将姓名排序，便于保留大写版本的姓名
使用fuzzywuzzy进行模糊匹配
建立应该姓名和代替姓名间的map
存储到二进制文件便于下次读取
'''
def mergeNames():
    # 从文件中加载set
    with open('set.pkl', 'rb') as set_file:
        name_set = pickle.load(set_file)
        print(len(name_set))
    with open('map.pkl','rb') as map_file:
        name_mappings = pickle.load(map_file)

    # 对names进行转换，并备份
    name_list = list(name_set)
    name_list.sort()

    for index, name in enumerate(name_list):
        print(index)
        if index % 1000 == 0 and index > 0:
            # 将set保存到文件
            with open('set.pkl', 'wb') as set_file:
                pickle.dump(name_set, set_file)
            with open('map.pkl', 'wb') as map_file:
                pickle.dump(name_mappings, map_file)

        name_set.discard(name)

        similar_names = process.extractBests(name, name_set, score_cutoff=90, scorer=fuzz.ratio)

        for similar_name, score in similar_names:
            if similar_name != name:
                name_set.discard(similar_name)
                name_mappings[similar_name] = name
                print(similar_name, name)

    print(len(name_mappings))
    with open('set.pkl', 'wb') as set_file:
        pickle.dump(name_set, set_file)
    with open('map.pkl', 'wb') as map_file:
        pickle.dump(name_mappings, map_file)


'''
根据map替换导演、演员、主演的姓名为同一版本
'''
def afterMerge():
    raw_data = pd.read_csv('./movie_info.csv', encoding='utf-8')
    with open('map.pkl', 'rb') as map_file:
        name_mappings = pickle.load(map_file)

    # 替换列中的值
    columns_to_replace = ['movie_director', 'main_actor', 'movie_actor']
    for column in columns_to_replace:
        # 使用 str.split(',') 将逗号分隔的姓名拆分成列表，并处理空值
        raw_data[column] = raw_data[column].apply(
            lambda x: ', '.join(
                [name_mappings.get(name.strip(), name.strip()) for name in str(x).split(',') if name.strip()])
        )

    # 将空值替换为空字符串
    raw_data = raw_data.replace({'': None, 'nan': None})
    raw_data.to_csv('./movie_info.csv', index=False, encoding='utf-8')


'''
根据不同需要，调用不同函数，可微调
'''
# removeRedundantMarks()
# beforeMerge()
# mergeNames()
afterMerge()