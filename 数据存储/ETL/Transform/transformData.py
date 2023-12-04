import pickle
from collections import defaultdict

import pandas as pd
import re
from datetime import datetime

from fuzzywuzzy import process, fuzz


def mergeMovies():
    # 电影名称和导演相同的视作同一部电影
    # 读取output.csv
    output = pd.read_csv('./new_movies_info_整理title.csv', encoding='utf-8')

    # 将电影名称和导演转换为小写，以便进行忽略大小写的比较
    output['Title'] = output['Title'].str.lower()
    output['Directors'] = output['Directors'].str.lower()

    # 去除movie_id和director相同的行，只保留第一项
    output.drop_duplicates(subset=['Title','Directors'], keep='first', inplace=True)

    # 保存修改后的数据到newids.csv文件
    output.to_csv('./new_movies_info_整理title.csv', index=False, encoding='utf-8')


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


def removeRedundantMarks():
    raw_data = pd.read_csv('./output_with_time.csv', encoding='utf-8')
    for column in ['movie_director', 'movie_starring', 'movie_actor']:
        # 遍历指定列，替换所有字符串中的多余双引号
        raw_data[column] = raw_data[column].str.replace('"', '')

    # 将处理后的数据保存到新文件
    raw_data.to_csv('./output_cleaned.csv', index=False, encoding='utf-8')


def removeVersionFromTitle():
    raw_data = pd.read_csv('./output_merge_name.csv', encoding='utf-8')

    unique_versions = {'DVD', 'Blu-ray', 'VHS', 'UMD for PSP'}

    def remove_version_info(movie_title):
        # 确保 movie_title 是一个字符串
        if not isinstance(movie_title, str):
            return movie_title
        # 使用正则表达式获取最后一部分数据
            # 尝试匹配 [] 或者 ()
        bracket_match = re.search(r'\s*([\[(][^\])]+[\])])\s*$', movie_title)

        # 如果匹配到 [] 或者 ()，则删除
        if bracket_match:
            last_part = bracket_match.group(1)
            for version in unique_versions:
                if version.lower() in last_part.lower():
                    return re.sub(fr'\s*{re.escape(bracket_match.group(1))}\s*$', '', movie_title).strip()

        # 否则，使用空格分割的最后一部分
        else:
            last_part_match = re.search(r'\s*([^ ]+)\s*$', movie_title)
            if last_part_match:
                last_part = last_part_match.group(1)
                for version in unique_versions:
                    if version.lower() in last_part.lower():
                        return re.sub(fr'\s*{re.escape(last_part)}\s*$', '', movie_title).strip()
        return movie_title


    # 应用remove_version_info函数来清理电影名
    raw_data['movie_title'] = raw_data['movie_title'].apply(remove_version_info)
    raw_data.to_csv('./testCaseResult.csv', index=False, encoding='utf-8')
    # print(raw_data)


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
    # 使用正则表达式一次性替换所有匹配的名字
    # raw_data = pd.read_csv('./testCase.csv', encoding='utf-8')
    # raw_data = pd.read_csv('./output_with_time.csv', encoding='utf-8')
    # for column in ['movie_director', 'movie_starring', 'movie_actor']:
    #     for original_name, mapped_name in name_mappings.items():
    #         regex_pattern = r'\b' + re.escape(original_name) + r'\b'
    #         raw_data[column].replace(regex_pattern, value=mapped_name, regex=True, inplace=True)
    # raw_data.to_csv('./output_merge_name.csv', index=False, encoding='utf-8')


def afterMerge():
    raw_data = pd.read_csv('./new_movies_info_整理title.csv', encoding='utf-8')
    with open('map.pkl', 'rb') as map_file:
        name_mappings = pickle.load(map_file)

    # 替换列中的值
    columns_to_replace = ['Directors', 'main_actor', 'Actors']
    for column in columns_to_replace:
        # 使用 str.split(',') 将逗号分隔的姓名拆分成列表，并处理空值
        raw_data[column] = raw_data[column].apply(
            lambda x: ', '.join(
                [name_mappings.get(name.strip(), name.strip()) for name in str(x).split(',') if name.strip()])
        )

    # 将空值替换为空字符串
    raw_data = raw_data.replace({'': None, 'nan': None})
    raw_data.to_csv('./new_movies_info_整理title.csv', index=False, encoding='utf-8')


def addResource():
    # 电影名称和导演相同的视作同一部电影
    # 读取output.csv
    output = pd.read_csv('./testCaseResult.csv', encoding='utf-8')

    output['movie_resource'] = 'https://www.amazon.com/dp/' + output['movie_id']

    output = output[['movie_id','movie_title','movie_release_date','movie_genre','movie_director','movie_starring','movie_actor','movie_version','movie_rating','movie_format','movie_language','movie_related_id','movie_resource']]

    # 保存修改后的数据到newids.csv文件
    output.to_csv('./testCaseResult.csv', index=False, encoding='utf-8')


def deleteErrorData():
    # 读取CSV文件
    output = pd.read_csv('./new_movies_info_整理title.csv', encoding='utf-8')

    # 删除 'Title' 列为空的行
    output = output.dropna(subset=['Title'])

    # 保存修改后的DataFrame
    output.to_csv('./new_movies_info_整理title.csv', index=False, encoding='utf-8')


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

mergeMovies()
# addExtraTime()
# removeRedundantMarks()
# beforeMerge()
# mergeNames()
# afterMerge()
# removeVersionFromTitle()
# addResource()
# deleteErrorData()
# mapID()
# with open('id_mappings.pkl', 'rb') as map_file:
#     id_mappings = pickle.load(map_file)
#     print(id_mappings)
