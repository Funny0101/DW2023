import pandas as pd
import numpy as np


'''
清除表中所有的引号
'''
def removeRedundantMarks():
    # 读取 CSV 文件
    raw_data = pd.read_csv('./movie_info.csv', encoding='utf-8')

    # 清除表中所有的单双引号
    raw_data = raw_data.apply(lambda s: s.replace("\'", '').replace('\"', '') if isinstance(s, str) else s)

    # 将处理后的数据保存到新文件
    raw_data.to_csv('./movie_info.csv', index=False, encoding='utf-8')


'''
去除电影标题中包含的版本信息
便于更好的去重
'''
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


'''
进行电影信息去重
电影名称和导演相同认定为同一部电影
建立数据血缘关系
'''
def merge_movies():
    # 读取CSV文件
    df = pd.read_csv('movie_info.csv')

    # 1.删除大概率错误数据
    df = df.dropna(subset=['movie_title'])
    df = df.dropna(subset=['movie_id'])

    # 2.去除movie_id重的数据
    df.drop_duplicates(subset=['movie_id'], keep='first', inplace=True)

    # 3.去重并记录数据血缘，认为电影名和导演都相同的为同一部电影
    # 选择除 movie_id,movie_title, movie_director外的所有列
    non_movie_id_columns = df.columns.difference(['movie_id','movie_title', 'movie_director'])
    # 使用 apply 函数将 'movie_id' 列添加到非 'movie_id' 列的末尾
    df[non_movie_id_columns] = df[non_movie_id_columns].apply(
        lambda x: x.astype(str) + '_' + df['movie_id'].astype(str))
    # 将原本为空值的地方恢复为空值
    df[non_movie_id_columns] = df[non_movie_id_columns].replace(r'^nan_[a-zA-Z0-9]{10}$', pd.NA, regex=True)
    # 得到每个组的第一行数据
    first_rows = df.groupby(['movie_title', 'movie_director']).transform('first')
    # 填充空白位置
    result_df = df.combine_first(first_rows)
    # 去除重复数据 保留第一项
    # result_df.drop_duplicates(subset=['movie_title', 'movie_director'], keep='first', inplace=True)
    # 建立数据来源的映射表
    result_of = result_df.copy()
    result_of[non_movie_id_columns] = result_of[non_movie_id_columns].apply(lambda x: x.str.split('_').str[-1])
    # 使用矢量化操作将匹配的值替换为 NaN
    mask = (result_of[non_movie_id_columns].values == result_of['movie_id'].values[:, np.newaxis])
    result_of[non_movie_id_columns] = np.where(mask, pd.NA, result_of[non_movie_id_columns].values)

    # 去除末尾的movie_id
    result_df[non_movie_id_columns] = result_df[non_movie_id_columns].apply(lambda x: x.str.split('_').str[:-1].str.join(''))

    # 4.保存结果
    # 保存去重结果
    result_df.to_csv('movie_info_deduplication.csv', index=False)
    # 保存映射关系
    result_of.to_csv('movie_info_mapping.csv', index=False)


'''
以下可以进行组合操作
'''
# removeRedundantMarks()
# removeVersionFromTitle()
merge_movies()